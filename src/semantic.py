# Semantic script

def search_semantic_with_scores(vectorstore, query, k=3):
    """
    Runs a FAISS semantic search and returns the top K documents along with their L2 distance scores.
    """
    results = vectorstore.similarity_search_with_score(query, k=k)
    return results

def display_semantic_results(scored_results):
    print("Top 3 Semantic Search Results\n" + "="*50)
    
    # Slice the list to ensure we only process a maximum of 3 results
    for rank, (doc, score) in enumerate(scored_results[:3], 1):
        
        # 1. Parse the title and text out of the page_content string
        lines = doc.page_content.split('\n')
        
        # Adding a quick safety check just in case a document got formatted weirdly
        product_title = lines[0].replace("Product Title: ", "") if len(lines) > 0 else "Unknown Title"
        review_text = lines[2].replace("Review Text: ", "") if len(lines) > 2 else "No Review Text"
        
        # 2. Truncate the review text to ~200 characters
        if len(review_text) > 200:
            truncated_review = review_text[:200].rsplit(' ', 1)[0] + "..."
        else:
            truncated_review = review_text
            
        # 3. Format the rating as visual stars
        rating = int(doc.metadata.get('rating', 0))
        stars = "⭐" * rating
        
        # 4. Display the formatted result
        # Note the label change to 'L2 Distance' so users know lower is better!
        print(f"#{rank} | L2 Distance: {score:.3f}") 
        print(f"Product: {product_title}")
        print(f"Rating:  {stars} ({rating}/5)")
        print(f"Review:  {truncated_review}")
        print("-" * 50)