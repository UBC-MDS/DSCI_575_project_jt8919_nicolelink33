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
**Query 1: "sewing machine"**

Question:
sewing machine

Answer:
sewing machine

Assistant: 
Sewing machine

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | no |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | yes |

Comments:

- Did not cite product ASIN

**Query 2: "acrylic paint"**

Question:
acrylic paint

Answer:
Based on the provided review, the best answer is that the product is a **paint**. The reviewer mentions that the paint is used for various projects, such as rock painting and door painting, and highlights the fact that it has a matte finish, quick drying, and blending capabilities. Additionally, they express satisfaction with the color selection and the use of different colors for various projects. However, the reviewer also mentions that the yarn lacks drape and that it might be challenging to work with at first.

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | partial yes\* |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | yes |

Comments:

- \*Partial yes because all the information provided from the LLM came from the reviews, but it associating the yarn review with our paint question, which is not fully correct
- Did not cite product ASIN

**Query 3: "Singer 5532"**

Question:
Singer 5532

Answer: 
The product ASIN: B0092RC3YI is the SINGER 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate. Its rating is 5.0/5 and reviewed by 50 people. The product features a 5532 HEAVY DUTY SEWING MACHINE that sews 1,100 stitches per minute. It comes with an all-metal frame, but is not an all-metal sewing machine. It has an all-metal frame, but is not an all-metal sewing machine. It is

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | no |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | no |

Comments:

- Correctly identified the product ASIN, title, and rating. Not sure about accuracy of "reviewed by 50 people"
- The response ends mid-sentence on "It is"
- Fluency drops at the second half of the response: "It comes with an all-metal frame, but is not an all-metal sewing machine. It has an all-metal frame, but is not an all-metal sewing machine."

**Query 4: "Animal stickers"**

Question:
Animal stickers

Answer:
The animal stickers mentioned in the product reviews are:

1. Knaid Butterfly Dragonfly Insects Stickers Set (240 Pieces) - PET Transparent Waterproof Decorative Decals for Scrapbook DIY Crafts Album Bullet Journal Planner Water Bottles Phone Cases Laptops
2. Aromoty Flower Gold foil Holographic Stickers Set( 120 pieces with 3 Themes)-Resin Transparent Waterproof Stickers,Butterfly,Vintage Daily Planner Stickers for Scrapbook Junk Bullet Journals, Laptop,Water bottles Decor for kids adults (Flower B- Warm)
3. 120 Pieces Vintage Scrap

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | yes |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | no |

Comments:

- Did not cite product ASIN
- Bad spacing in second bulletpoint because the revidw had bad spacing "Stickers,Butterfly,Vintage"
- Stopped mid-sentence for the third bulletpoint

**Query 5: "Purple gel pen"**

Question:
Purple gel pen

Answer:
The purple gel pen mentioned in the product review has a reputation for experiencing issues with drying and being run dry after use. This issue affects several different components of the product, including the pen itself and the nib itself. The reviewer notes that the pen's nib is coated with a layer of dried ink, which can lead to the pen being emptied when used. This issue is particularly problematic for users who are using the pen for long periods of time, such as for drawing or painting.

The reviewer also mentions a concern about the product's consistency, as the nib is coated with ink that spreads too quickly. This can create a noticeable scratch on the

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | no |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | yes |

Comments:

- Did not cite product ASIN

**Query 6: "cute embroidery patterns"**

Question:
cute embroidery patterns

Answer:
cute embroidery patterns

Assistant: cute embroidery patterns

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | no |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | no |

**Query 7: "yarn made of natural fibers"**

Question:
yarn made of natural fibers

Answer:
The yarn made of natural fibers is B0BWSF1HPY, which has a rating of 5.0/5 and was reviewed by a user named "Fraggle." The reviewer found it to be a good yarn and appreciated its soft and dense feel. They also mentioned that the yarn was easy to work with and was suitable for various projects. However, they did have a few issues with the yarn, such as knots and a slightly bad appearance. Despite these issues, the reviewer was impressed with the yarn's quality and continued to use it for crafting purposes. 

On the other hand, the yarn made of natural

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | no |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | yes |

Comments:

- Correctly cited product ASIN, however, it mixed the review of the product B0BWSF1HPY with other product reviews. 
- Not complete because it answered 1 product correctly, but it missed another product in the context that is also yarn made of natural fibers
- Got cut off mid-sentence but the grammar overall is good

**Query 8: "best paint for wood"**

Question:
best paint for wood

Answer:
The best type of paint for wood is an acrylic paint that is specifically designed for wood construction. Acrylic paints can be applied to wood surfaces with ease and achieve a smooth, glossy finish that will not chip or peal off. They also require less maintenance than oil-based paints, as they do not contain solvents or other chemicals that can degrade the wood's finish. Additionally, acrylic paints are more environmentally friendly than oil-based paints, as they are made from natural ingredients and are less toxic to the environment. Acrylic paints are also available in a variety of colors and finishes, making it easy to achieve the desired look for various wood projects

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | no |
| Completeness | Does the answer address all aspects of the question? | yes |
| Fluency | Is the answer natural, clear, and easy to read? | yes |

Comments:

- Did not cite product ASIN
- The reviews did not mention anything about "acrylic paints are more environmentally friendly than oil-based paints"
- Response stops mid-sentence

**Query 9: "what's the best type of yarn to make clothes with"**

Question:
what's the best type of yarn to make clothes with

Answer:
Lion Brand Yarn Bonbons Yarn, Nature 8 x 28 yd/26 m

Assistant: The best type of yarn to make clothes with is Kona Cotton Capri, a fabric that features a light and airy feel, perfect for creating cozy and practical clothing items.

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | no |
| Completeness | Does the answer address all aspects of the question? | no |
| Fluency | Is the answer natural, clear, and easy to read? | yes |

Comments:

- Did not cite product ASIN
- The Answer recommends one product while the Assistant recommends another
- The product the Assistant recommends is not a type of yarn, it is a type of fabric

**Query 10: "what is a good type of yarn for a beginner"**

Question:
what is a good type of yarn for a beginner

Answer:
The product ASIN for Lion Brand Yarn 5800-526 Martha Stewart Glitter Eyelash Yarn, Brownstone is a beautiful yarn that adds a lovely, glamorous look to various projects. It is made of a soft pink yarn that reflects rainbow colors. If you are looking for a good yarn for beginning projects, this is a great option. The yarn has a touch of delicate pink and reflects sparkly rainbow colors. 

The product ASIN for Arm Knitting Yarn for Chunky Braided Knot Throw Blanket DIY, Soft Extra Cotton Washable Tube Bulky Giant Yarn for Weave Craft

| Dimension | What to assess | Quality |
| :--- | :--- | :--- |
| Accuracy | Is the answer factually correct based on the reviews? | yes |
| Completeness | Does the answer address all aspects of the question? | yes |
| Fluency | Is the answer natural, clear, and easy to read? | no |

Comments:

- Did not cite product ASIN
- Choppy response for the second half

### Results
How the RAG workflow is performing overall.

- Grammar and punctation is pretty good overall, answer is fairly clear and easy to read. However, most of the response stops mid-sentence.
- Inconsistent fluency, some responses seems like it was generated by pasting a few reviews together, generating a very choppy response.

2 limitations of your Hybrid RAG workflow.

- The model seems to be unable to distinguish that the different comments are talking about different products, it tends stitch together different product reviews into one. 
- Does not always cite the product ASIN even though we asked for it in the system prompt

Suggestions for how the workflow’s performance could be improved.

- Use a bigger model, this LLM is pretty small, it might generate better results with a bigger LLM
- Give the model a larger response length. It might get cut off mid sentence less often then. 
- Currently most of our queries are designed for simple product retrieval (eg. sewing machine), which our simple retrieval is already sufficient for. The LLM would be much more useful/applicable for more complex questions, like "which sewing machine is the most durable over a long time of use?"
