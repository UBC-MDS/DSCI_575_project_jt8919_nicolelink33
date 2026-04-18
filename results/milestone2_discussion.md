# Milestone 2 Discussion

## Model Choice and Rationale

- Started out with `HuggingFace` model `Qwen/Qwen2.5-0.5B` because it is a small and light model.




## Experimentation with System Prompt Variants
**System Prompt #1:**
```
prompt = ChatPromptTemplate.from_template(
"""
You are a helpful Amazon shopping assistant.
    Answer the question using ONLY the following context (real product reviews + metadata).
    Always cite the product ASIN when possible.

Context:
{context}

Question:
{input}

Answer:
"""
)
```

**System Prompt #2:**
```
prompt_idk = ChatPromptTemplate.from_template(
"""
You are a helpful Amazon shopping assistant.
    Answer the question using ONLY the following context (real product reviews + metadata).
    Always cite the product ASIN when possible.
    If the answer is present, extract and summarize it clearly.
    Do NOT say "I don't know" if the answer exists in the context.
    Only say "I don't know" if the context truly does not contain the answer.

Context:
{context}

Question:
{input}

Answer:
"""
)
```

| System Prompt #1 (Baseline) | System Prompt #2 (Constrained) |
| :--- | :--- |
| **Answer:**<br>The specific product that is green is the "Green Wax Seal Beads Macaron Green Sealing Wax Beads for Wax Seal Stamp Wedding Invitations Cards Gift Wrapping Letter Sealing (#17 Macaron Green)".<br><br>**Assistant:** The product is green, which is the color that is listed as the green wax seal beads in the description. | **Answer:**<br>I don't know<br><br>**Assistant:** Product ASIN: B0BRJPGGWW<br>Title: Green Wax Seal Beads Macaron Green Sealing Wax Beads for Wax Seal Stamp Wedding Invitations Cards Gift Wrapping Letter Sealing (#17 Macaron Green)<br>Rating: 4.0/5<br>Review: These are almost too pretty to use and melt. They are a lovely, rich shade of green. There are not very many in the pack considering it takes 2 or 3 for most seals.  Thy work just fine.<br>Product ASIN: B0B6C36KHY<br>Title: |

We tested two variations of system prompts, with **System Prompt #1** as our baseline, and **System Prompt #2** as a more constraint prompt to prevent hallucination of the model by forcing an "I don't know" when the context does not contain the answer. We found that **System Prompt #1** worked better with the current LLM model. From the above comparison table, we can see that given the same query and context, **System Prompt #1** is able to generate a reasonable and comprehensible response. However, one thing to note is that **System Prompt #1** failed the instruction of citing the ASIN. For **System Prompt #2**, the LLM answered *I don't know* even though the answer is present in the context. Furthermore, **System Prompt #2** returned the correct in the **Assistant** but as a raw context text. Therefore, we will proceed with **System Prompt #1** for the rest of the project because it works better for our chosen LLM model. 


## Hybrid RAG Evaluation:
### Manual Evaluation:


### Results

