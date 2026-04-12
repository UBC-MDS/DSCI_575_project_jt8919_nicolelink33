import sys
import os
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))
os.chdir(project_root)

import streamlit as st
import pickle
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from src.bm25 import search_bm25_with_scores
from src.semantic import search_semantic_with_scores


# -----------------------------------------------------------------------------
# 1. Load Data and Models (Cached)
# -----------------------------------------------------------------------------
# st.cache_resource ensures these heavy objects are only loaded once per session
@st.cache_resource
def load_search_engines():

    print("Loading search models into memory...") 

    # Load bm25 search model
    bm25_path = Path('models/bm25_metadata_index_2.pkl')
    if not bm25_path.exists():
        st.error(f"Could not find the index file at {bm25_path.absolute()}")
        return None, None

    with open(bm25_path, 'rb') as f:
        print("Loading BM25 index from pickle...")
        bm25_model = pickle.load(f)

    # Load semantic search model
    faiss_path = "models/faiss_index"
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