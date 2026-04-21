import sys
import os
from pathlib import Path

# project_root = Path(__file__).resolve().parent.parent
# if str(project_root) not in sys.path:
#     sys.path.append(str(project_root))
# os.chdir(project_root)

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
bm25_path = os.path.join(project_root, "models", "bm25_metadata_index_big.pkl")

import torch
import streamlit as st
import pickle
import transformers
from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from src.bm25 import search_bm25_with_scores
from src.semantic import search_semantic_with_scores
from src.hybrid import get_hybrid_retriever
from src.rag_pipeline import get_rag_chain
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


# -----------------------------------------------------------------------------
# 1. Load Data and Models (Cached)
# -----------------------------------------------------------------------------
@st.cache_resource
def load_search_engines():

    print("Loading search models into memory...") 

    # Load bm25 search model
    # bm25_path = Path("models/bm25_metadata_index_big.pkl")
    if not bm25_path.exists():
        st.error(f"Could not find the index file at {bm25_path.absolute()}")
        return None, None

    with open(bm25_path, 'rb') as f:
        print("Loading BM25 index from pickle...")
        bm25_model = pickle.load(f)

    # Load semantic search model
    faiss_path = "models/faiss_index_big"
    if not Path(faiss_path).exists():
        st.error(f"Could not find the FAISS index folder at {faiss_path}")
        return bm25_model, None
    
    print("Loading FAISS index and HuggingFace embeddings...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    semantic_model = FAISS.load_local(
        folder_path=faiss_path,
        embeddings=embeddings,
        allow_dangerous_deserialization=True
    )
    
    return bm25_model, semantic_model

bm25, semantic = load_search_engines()

# -----------------------------------------------------------------------------
# 2. Define Search Wrapper Functions
# -----------------------------------------------------------------------------
def run_bm25_search(query, model):
    return search_bm25_with_scores(model, query, k=3)

def run_semantic_search(query, model):
    return search_semantic_with_scores(model, query, k=3)

def get_ensemble(bm25_retriever, semantic_vectorstore, k=3, weights=[0.4, 0.6]):
    return get_hybrid_retriever(bm25_retriever, semantic_vectorstore, k=3, weights=[0.4, 0.6])

# -----------------------------------------------------------------------------
# 3. Build the Dashboard UI
# -----------------------------------------------------------------------------
st.title("🔍 Amazon Reviews Search Engine")
st.markdown("Search through product reviews or generate insights using AI.")

# Create Tabs
tab_search, tab_rag = st.tabs(["Search", "RAG"])

# =============================================================================
# TAB 1: SEARCH
# =============================================================================
with tab_search:
    st.subheader("Standard Search")
    
    # User Inputs (Note the added 'key' to prevent Streamlit duplicate ID errors)
    query = st.text_input("Enter your search query:", placeholder="e.g., 'battery life' or 'durable'", key="search_query")

    # Search Type Toggle
    search_type = st.radio(
        "Select Search Method:",
        ("BM25 (Keyword Match)", "Semantic (Meaning Match)"),
        horizontal=True,
        key="search_type_radio"
    )

    # Search Execution
    if st.button("Search", key="search_btn"):
        if not query:
            st.warning("Please enter a query first!")
        else:
            with st.spinner("Searching reviews..."):
                
                # Route to the correct function based on the radio button
                if "BM25" in search_type:
                    results = run_bm25_search(query, bm25)
                else:
                    results = run_semantic_search(query, semantic)
                
                # -----------------------------------------------------------------
                # 4. Display Results
                # -----------------------------------------------------------------
                st.markdown(f"**Top Results for:** '{query}'")
                
                if not results:
                    st.info("No reviews found matching your query.")
                else:
                    # Display each result nicely formatted
                    for i, (doc, score) in enumerate(results):
                        # 1. Extract metadata
                        metadata = doc.metadata
                        rating = metadata.get('rating', 'N/A')
                        price = metadata.get('price', 'N/A')
                        
                        # 2. Clean up the page_content
                        parts = doc.page_content.split('\n')
                        title = parts[0].replace("Product Title: ", "") if len(parts) > 0 else "Unknown Product"
                        review = parts[2].replace("Review Text: ", "") if len(parts) > 2 else doc.page_content

                        # 3. Render the UI Card
                        with st.container():
                            # Using columns to put Score and Rating side-by-side
                            col1, col2, col3 = st.columns([1, 1, 1])
                            # Check if score is a string (Hybrid Rank) or float (BM25/Semantic Score)
                            if isinstance(score, str):
                                col1.metric("Hybrid Match", score)
                            else:
                                col1.metric("Match Score", f"{score:.2f}")
                            col2.metric("Rating", f"{rating}/5 ⭐")
                            col3.metric("Price", f"${price}")

                            st.markdown(f"### {title}")
                            st.write(f"\"{review}\"")
                            st.divider()

# =============================================================================
# TAB 2: RAG (Retrieval-Augmented Generation)
# =============================================================================
with tab_rag:
    st.subheader("RAG Q&A")
    st.markdown("Ask a question, and the system will summarize an answer based on the top product reviews.")
    
    rag_query = st.text_input("Ask a question about the products:", 
                              placeholder="e.g., 'What are the main complaints about the yarn?'", 
                              key="rag_query_input")
    
    if st.button("Generate Answer", key="rag_btn"):
        if not rag_query:
            st.warning("Please enter a question first!")
        else:
            with st.spinner("Analyzing reviews and generating answer..."):
                
                # initialize LLM
                # generator = pipeline(
                #     "text-generation",
                #     model="Qwen/Qwen2.5-0.5B",
                #     torch_dtype = torch.float16,
                #     device="mps",
                #     trust_remote_code=True,
                #     max_new_tokens=128,
                #     do_sample=True,
                # )

                # llm = HuggingFacePipeline(pipeline=generator)

                llm = ChatGroq(model="llama-3.1-8b-instant")

                rag_chain = get_rag_chain(bm25, semantic, llm)

                # 1. Run the chain
                full_output = rag_chain.invoke(rag_query)

                # 2. Split the output into Context and Answer
                # # We split at "Question:" to separate the reviews from the response
                # parts = full_output.split("Question:")
                # context_block = parts[0].replace("Human:", "").replace("Context:", "").strip()
                
                # # Get the Answer specifically
                # answer_part = "I couldn't generate a summary."
                # if "Answer:" in full_output:
                #     answer_part = full_output.split("Answer:")[-1].strip()

                # 3. Display the AI Summary First (Clean text, no scroll box)
                st.subheader("🤖 AI Summary")
                st.write(full_output)

                st.divider()

                # # 4. Display the Reviews (Cleanly formatted)
                # st.subheader("📄 Related Reviews Used")
                
                # # We split the context block by "Product ASIN:" to show individual reviews
                # reviews = context_block.split("Product ASIN:")
                # for review in reviews:
                #     clean_review = review.strip()
    
                #     # SKIP the item if it contains your system prompt or is empty
                #     if not clean_review or "You are a helpful Amazon shopping assistant" in clean_review:
                #         continue
                    
                #     with st.container():
                #         # Add the prefix back for a clean look
                #         st.markdown(f"**Product ASIN:** {clean_review}")
                #         st.divider()