import sys
import os
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))
os.chdir(project_root)

import streamlit as st
import pandas as pd
import pickle
from langchain_community.retrievers import BM25Retriever
from src.utils import simple_tokenize
from src.bm25 import search_with_scores, display_top_results


# -----------------------------------------------------------------------------
# 1. Load Data and Models (Cached)
# -----------------------------------------------------------------------------
# st.cache_resource ensures these heavy objects are only loaded once per session
@st.cache_resource
def load_search_engines():
    # TODO: Import and initialize your actual BM25 and Semantic models here.
    # For example: loading the BM25 index and the Hugging Face embedding model.
    print("Loading search models into memory...") 

    #bm25_path = Path("data/bm25_retriever.pkl")
    bm25_path = Path('models/bm25_metadata_index_2.pkl')

    if not bm25_path.exists():
        st.error(f"Could not find the index file at {bm25_path.absolute()}")
        return None, None

    with open(bm25_path, 'rb') as f:
        print("Loading BM25 index from pickle...")
        bm25_model = pickle.load(f)

    # Returning dummy objects for semantic for now:
    semantic_model = "SEMANTIC_READY"

    return bm25_model, semantic_model

bm25, semantic = load_search_engines()

# -----------------------------------------------------------------------------
# 2. Define Search Wrapper Functions
# -----------------------------------------------------------------------------
def run_bm25_search(query, model):
    # TODO: Replace with your actual BM25 function execution
    # return your_bm25_function(query, model)
    

    # Mock return data
    #return [
    #   {"text": "This product was amazing, highly recommend!", "rating": 5.0},
    #    {"text": "Good value for the price, but shipping was slow.", "rating": 4.0}
    #]
    return search_with_scores(model, query, k=3)

def run_semantic_search(query, model):
    # TODO: Replace with your actual semantic search function execution
    # return your_semantic_function(query, model)

    # Mock return data
    return [
        {"text": "Absolutely stellar quality and performance.", "rating": 5.0},
        {"text": "It works as expected. Nothing special.", "rating": 3.0}
    ]

# -----------------------------------------------------------------------------
# 3. Build the Dashboard UI
# -----------------------------------------------------------------------------
st.title("🔍 Amazon Reviews Search Engine")
st.markdown("Search through product reviews using exact keyword matching or semantic meaning.")

# User Inputs
query = st.text_input("Enter your search query:", placeholder="e.g., 'battery life' or 'durable'")

# Search Type Toggle
search_type = st.radio(
    "Select Search Method:",
    ("BM25 (Keyword Match)", "Semantic (Meaning Match)"),
    horizontal=True
)

# Search Execution
if st.button("Search"):
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
            st.subheader(f"Top Results for: '{query}'")
            
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
                    # Your content format: "Product Title: ... \n Category: ... \n Review Text: ..."
                    parts = doc.page_content.split('\n')
                    title = parts[0].replace("Product Title: ", "") if len(parts) > 0 else "Unknown Product"
                    review = parts[2].replace("Review Text: ", "") if len(parts) > 2 else doc.page_content

                    # 3. Render the UI Card
                    with st.container():
                        # Using columns to put Score and Rating side-by-side
                        col1, col2, col3 = st.columns([1, 1, 1])
                        col1.metric("Match Score", f"{score:.2f}")
                        col2.metric("Rating", f"{rating}/5 ⭐")
                        col3.metric("Price", f"${price}")

                        st.markdown(f"### {title}")
                        st.write(f"\"{review}\"")
                        st.divider()