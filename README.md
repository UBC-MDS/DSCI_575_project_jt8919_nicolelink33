# Arts and Crafts Product Search:
### DSCI_575_project_jt8919_nicolelink33
Authors: Jennifer Tsang, Nicole Link

This is an interactive tool which allows for search and retrieval of arts and crafts supplies based on an Amazon 2023 reviews dataset.

## Description
### Dataset: 
The dataset contains Amazon reviews collected in 2023 by McAuley Lab. It contains reviews on products that belong to the Arts and Crafts category. Our dashboard specifically searches from a subset of this dataset. The subset removed very short reviews (< 20 characters), stratified the dataset by short and long reviews, and by the number of stars, and sampled 50 reviews per strata, prioritizing the most helpful reviews. 

### Data Proecessing:


### Retrieval Workflows:



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
Open the project repo in VSCode or an editor of your choice, and ensure that in the VSCode terminal you navigate to the project root and activate the 575-app environment. 
```bash
code .
____________
```

Open notebooks/milestone1_exploration.ipynb and run all cells. This does necessary data downloading and processing. 

Open app/app.py and run the dashboard locally:
```bash
streamlit run app/app.py
```

Open the dashboard in your browser. 
http://localhost:8501/


## Attribution

Generative AI tools (Google Gemini) were used to assist with code generation and documentation drafting. All generated content was reviewed and edited by the authors to ensure accuracy and quality.