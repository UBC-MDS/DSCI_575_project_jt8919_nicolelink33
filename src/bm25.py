# BM25 Script

import numpy as np

# Does BM25 search and returns the top 3 results with a score:
def search_bm25_with_scores(retriever, query, k=3):
    """
    Runs a BM25 search and returns the top K documents along with their exact scores.
    """
    # Tokenize the query using the same function used to build the index
    tokenized_query = retriever.preprocess_func(query)
    
    # Get the raw BM25 scores for all document in the dataset
    all_scores = retriever.vectorizer.get_scores(tokenized_query)
    
    # Find the index positions of the top 'k' highest scores
    top_k_indices = np.argsort(all_scores)[::-1][:k]
    
    # Match the highest scores back to their original LangChain Documents
    results = []
    for idx in top_k_indices:
        doc = retriever.docs[idx]
        score = all_scores[idx]
        results.append((doc, score))
        
    return results