import re
import math

# Tokenization function
def simple_tokenize(text):
    # Lowercase everything
    text = text.lower()
    # Remove everything except letters, numbers, spaces, and hyphens
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    # Split into a list of words
    return text.split()

def display_results(scored_results, k=3, title="Top Search Results", score_label="Score"):
    """
    To display search results. Defaults outputs the top k results.
    """
    print(f"{title}\n" + "="*50)
    
    # Slice the list to ensure we only process a maximum of k results
    for rank, (doc, score) in enumerate(scored_results[:k], 1):
        
        # Parse the title and text out of the page_content string
        lines = doc.page_content.split('\n')
        product_title = lines[0].replace("Product Title: ", "") if len(lines) > 0 else "Unknown Title"
        review_text = lines[2].replace("Review Text: ", "") if len(lines) > 2 else "No Review Text"
        
        # Truncate the review text to ~200 characters
        if len(review_text) > 200:
            truncated_review = review_text[:200].rsplit(' ', 1)[0] + "..."
        else:
            truncated_review = review_text
            
        # Format the rating as visual stars
        raw_rating = doc.metadata.get('rating', 0)
        
        # Check if the rating is NaN or None
        if raw_rating is None or (isinstance(raw_rating, float) and math.isnan(raw_rating)):
            rating = 0
            stars = "No rating"
        else:
            rating = int(raw_rating)
            stars = "⭐" * rating
        
        # Display the formatted result
        # Standardized to 3 decimal places for both to keep it uniform
        print(f"#{rank} | {score_label}: {score:.3f}")
        print(f"Product: {product_title}")
        print(f"Rating:  {stars} ({rating}/5)")
        print(f"Review:  {truncated_review}")
        print("-" * 50)