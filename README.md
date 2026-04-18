# Arts and Crafts Product Search
### DSCI_575_project_jt8919_nicolelink33
Authors: Jennifer Tsang, Nicole Link

This is an interactive tool which allows for search and retrieval of arts and crafts supplies based on an [Amazon 2023 reviews dataset](https://amazon-reviews-2023.github.io/).

## Description
### Dataset: 
The dataset contains Amazon reviews collected in 2023 by McAuley Lab. It contains reviews on products that belong to the Arts and Crafts category. Our dashboard specifically searches from a subset of this dataset. The subset removed very short reviews (< 20 characters), stratified the dataset by short and long reviews, and by the number of stars, and sampled 50 reviews per strata, prioritizing the most helpful reviews. 

### Data Processing:
To prepare the sampled subset for search indexing, the tabular data was transformed into LangChain `Document` objects. We engineered a dense text string for the `page_content` by concatenating the product title, category, and review text. All structured attributes such as numerical ratings, price, and helpful votes were separated and preserved as queryable metadata. For lexical search compatibility, the text underwent preprocessing using a custom tokenizer to convert characters to lowercase, remove punctuation, and split strings into discrete words.

### Retrieval Workflows:
The system employs a dual-engine architecture to retrieve relevant documents based on user queries:

- **Lexical Search (BM25)**: A sparse retrieval engine that uses a custom tokenizer to match exact keywords.

- **Semantic Search (FAISS)**: A dense vector database powered by Facebook AI Similarity Search. Documents and user queries are embedded into a vector space using `sentence-transformers` and `all-MiniLM-L6-v2` model, allowing the system to retrieve results based on contextual meaning.

### RAG Pipeline Workflow Diagram
[](img/rag_pipeline.png)






## Instructions to Run Locally:

### Clone the repository
Using HTTPS:
```bash
git clone https://github.com/UBC-MDS/DSCI_575_project_jt8919_nicolelink33.git
```

Or using SSH:
```bash
git clone git@github.com:UBC-MDS/DSCI_575_project_jt8919_nicolelink33.git
```

Navigate to the project root:
```bash
cd DSCI_575_project_jt8919_nicolelink33
```
Create the environment

```bash
conda env create -f environment.yml
conda activate 575-app
```
Open `notebooks/milestone1_exploration.ipynb` in VSCode or an editor of your choice, and ensure that in VSCode you are using the `575-app` environment. Run all cells in this notebook. This does necessary data downloading, data processing, and model building. 
```bash
code notebooks/milestone1_exploration.ipynb
```

To run the dashboard locally, in terminal:
```bash
streamlit run app/app.py
```

Open the dashboard in your browser. 
http://localhost:8501/


## Attribution

Authors: Jennifer Tsang, Nicole Link

Generative AI tools (Google Gemini) were used to assist with code generation and documentation drafting. All generated content was reviewed and edited by the authors to ensure accuracy and quality.