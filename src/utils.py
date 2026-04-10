import re

# Tokenization function
def simple_tokenize(text):
    # Lowercase everything
    text = text.lower()
    # Remove everything except letters, numbers, spaces, and hyphens
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    # Split into a list of words
    return text.split()