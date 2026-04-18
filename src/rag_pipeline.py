import sys
from pathlib import Path

# Ensure the project root is in the path so src can be found
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from src.hybrid import get_hybrid_retriever

# RAG Pipeline script

# Context building function
def build_context(docs):
    context_parts = []
    for doc in docs:
        content = doc.page_content
        
        # 1. Extract the Title
        try:
            title = content.split("Product Title: ")[1].split("Category: ")[0].strip()
        except IndexError:
            title = "Unknown Product"

        # 2. Extract the Review Text 
        # This takes everything appearing after "Review Text: "
        try:
            review = content.split("Review Text: ")[1].strip()
        except IndexError:
            review = "No review text available."

        # 3. Assemble the formatted string
        entry = (
            f"Product ASIN: {doc.metadata.get('parent_asin', 'N/A')}\n"
            f"Title: {title}\n"
            f"Rating: {doc.metadata.get('rating', 'N/A')}/5\n"
            f"Review: {review}"
        )
        context_parts.append(entry)
    
    return "\n\n".join(context_parts)


# Prompt template
def get_prompt_template():
    # baseline prompt
    prompt1 = ChatPromptTemplate.from_template(
    """
    You are a helpful Amazon shopping assistant.
        Answer the question using ONLY the following context (real product reviews + metadata).
        Always cite the product ASIN when possible.

    Context:
    {context}

    Question:
    {input}

    Answer:
    """
    )
    return prompt1


# LLM

def get_rag_chain(bm25_model, semantic_vectorstore, llm):
    """
    Initializes the hybrid retriever and constructs the LCEL RAG chain.
    """
    
    # 1. Get the hybrid retriever from hybrid script
    ensemble_retriever = get_hybrid_retriever(bm25_model, semantic_vectorstore, k=5)

    # 2. Get prompt template
    prompt = get_prompt_template()

    # 3. Construct the Chain
    rag_chain = (
        {
            "context": ensemble_retriever | build_context,
            "input": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain