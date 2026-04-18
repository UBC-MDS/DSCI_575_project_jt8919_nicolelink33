from langchain_classic.retrievers import EnsembleRetriever

def get_hybrid_retriever(bm25_retriever, semantic_vectorstore, k=3, weights=[0.4, 0.6]):
    """
    Returns a configured EnsembleRetriever object to be used in LangChain chains.
    """
    # Configure Semantic Retriever
    semantic_retriever = semantic_vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    
    # Configure BM25 Retriever
    bm25_retriever.k = k

    # Create the Ensemble
    ensemble_retriever = EnsembleRetriever(
        retrievers=[bm25_retriever, semantic_retriever],
        weights=weights
    )
    
    return ensemble_retriever