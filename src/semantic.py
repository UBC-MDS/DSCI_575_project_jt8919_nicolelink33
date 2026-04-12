# Semantic script

def search_semantic_with_scores(vectorstore, query, k=3):
    """
    Runs a FAISS semantic search and returns the top K documents along with their L2 distance scores.
    """
    results = vectorstore.similarity_search_with_score(query, k=k)
    return results