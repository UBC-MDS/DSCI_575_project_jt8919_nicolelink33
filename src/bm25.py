# BM25 Script

import numpy as np

# Does BM25 search and returns the top 3 results with a score:
def search_with_scores(retriever, query, k=3):
    """
    Runs a BM25 search and returns the top K documents along with their exact scores.
    """
    # 1. Tokenize the query using the exact same function you used to build the index
    tokenized_query = retriever.preprocess_func(query)
    
    # 2. Get the raw BM25 scores for EVERY document in your entire dataset
    all_scores = retriever.vectorizer.get_scores(tokenized_query)
    
    # 3. Find the index positions of the top 'k' highest scores using NumPy
    top_k_indices = np.argsort(all_scores)[::-1][:k]
    
    # 4. Match the highest scores back to their original LangChain Documents
    results = []
    for idx in top_k_indices:
        doc = retriever.docs[idx]
        score = all_scores[idx]
        results.append((doc, score))
        
    return results



# Displays the top 3 results with a score:
def display_top_results(scored_results):
    print("Top 3 Search Results\n" + "="*50)
    
    # Slice the list to ensure we only process a maximum of 3 results
    for rank, (doc, score) in enumerate(scored_results[:3], 1):
        
        # 1. Parse the title and text out of the page_content string
        # Our format was: Title \n Category \n Text
        lines = doc.page_content.split('\n')
        product_title = lines[0].replace("Product Title: ", "")
        review_text = lines[2].replace("Review Text: ", "")
        
        # 2. Truncate the review text to ~200 characters
        if len(review_text) > 200:
            truncated_review = review_text[:200].rsplit(' ', 1)[0] + "..."
        else:
            truncated_review = review_text
            
        # 3. Format the rating as visual stars
        # We grab the rating from the metadata and convert the float to an integer
        rating = int(doc.metadata.get('rating', 0))
        stars = "⭐" * rating
        
        # 4. Display the formatted result
        print(f"#{rank} | Score: {score:.2f}")
        print(f"Product: {product_title}")
        print(f"Rating:  {stars} ({rating}/5)")
        print(f"Review:  {truncated_review}")
        print("-" * 50)
