# Final Discussion

## Step 1: Improve Your Workflow

### Dataset Scaling
- Number of products used
- Changes to sampling strategy (if any)

### LLM Experiment
- Models compared (name, family, size)
- Results and discussions
    - Prompt used (copy it here)
    - Results
- Which model you chose and why

For milestone 2, we used the smallest local HuggingFace model, Qwen2.5-0.5B, as we were worried about computational resources, and just wanted to get our RAG pipeline working first. We noted in Milestone 2 that the performance of this model was not very good, therefore for Milestone 3 we wanted to upgrade to a more advanced model. We chose to use Groq's Llama-3.1 8B Instant model. This model runs about 560 tokens per second, and is fairly compact, but still is listed as providing strong performance for many practical applications. The prompt we used is shown below:
```python
prompt1 = ChatPromptTemplate.from_template(
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
```
Results:
Query 1: "sewing machine"
| Qwen2.5-0.5B Results | Groq Llama-3.1 8B Results |
| :--- | :--- |
|  Human: 
    You are a helpful Amazon shopping assistant.
        Answer the question using ONLY the following context (real product reviews + metadata).
        Always cite the product ASIN when possible.

    Context:
    Product ASIN: B07YZV2485
Title: Unknown Product
Rating: 5.0/5
Review: I can’t speak for how good this would be in a machine, but it works very well for hand sewing. A nice selection of good quality colors.

Product ASIN: B087PBSF55
Title: Unknown Product
Rating: 5.0/5
Review: Great for the beginner or the person just taking up sewing again.  This small sewing machine has many of the features of a full-size machine.  It offers a variety of stitches, sews backward or forward, operates with bobbins, and uses either a power adapter or batteries.  It runs smoothly delivering a smooth, regular stitch.  It has a foot pedal for those who are used to having one.  Really pleased wit this energetic sewing machine!

Product ASIN: B097FPLKP2
Title: SINGER | 4423 Heavy Duty Sewing Machine & Beginners & Sewing Machine Accessory Kit, Including 9 Presser Feet, Twin Needle, and Case, Clear - Sewing Made Easy
Rating: 2.0/5
Review: I was looking for something that could sew jeans and such heavy fabrics or multiple layered fabrics. Thought this one would be great as the name itself says heavy duty. Machine is super easy to understand as well as to start using. This arrived the next day I ordered it. These are the only reasons to give these stars . When I unboxed it, I found there was a threaded spinner white bobbin inside already and a same whistle color thread spinner bobbin in the thread spool holder and needle was threaded as well. I believe no new machine comes With threads ready like this. Hence this is definitely used by someone but packed in a new box while sending the machine to me. I did not pay for used machine in the first place and I was very unhappy with when found I received a used machine for the money given. After all decided to test the machine to see if it works fine. Stitches were lose even with the right adjustments made, stitches were really awkward for the machine it is.

Product ASIN: B09817YZGQ
Title: Unknown Product
Rating: 5.0/5
Review: I am very happy with my sewing machine. I usually sew by hand, this is my first ever and Very happy with it.

Product ASIN: B09ZYSMSHD
Title: Unknown Product
Rating: 5.0/5
Review: Good delivery and useful ruler for sewing machine

Product ASIN: B08Y5NW6XN
Title: Magicfly Mini Sewing Machine for Beginner, Dual Speed Portable Sewing Machine Machine with Extension Table, Light, Sewing Kit for Household, Travel
Rating: 5.0/5
Review: This little sewing machine works perfect and very easy to use! Not to mention it is super cute

Product ASIN: B097FPLKP2
Title: SINGER | 4423 Heavy Duty Sewing Machine & Beginners & Sewing Machine Accessory Kit, Including 9 Presser Feet, Twin Needle, and Case, Clear - Sewing Made Easy
Rating: 5.0/5
Review: Packaged well, fast shipping. This sewing machine is easy to use, VERY fast and honestly I’m so pleased with this machine!!

Product ASIN: B08LYPVBJ8
Title: Unknown Product
Rating: 5.0/5
Review: This VOSDANS Travel Sewing Machine Bag with a Cover is perfect for my sewing machine. The cover is nice but the bag is great. The bottom has a removable piece for easy storage. There are pockets for the extras.<br /><br />My sewing machine sometimes sits without use for a while and the cover will be great for keeping dust off of it. The bag is great for taking it to be repaired or to a family member's home for sewing nights. The quality of both the bag and the cover is extraordinary.<br /><br />I will be recommending this VOSDANS Travel Sewing Machine Bag with a Cover to family and friends.

Product ASIN: B01LETBN24
Title: Janome 2212 Sewing Machine Includes Exclusive Bonus Bundle
Rating: 1.0/5
Review: This sewing machine is a complete pos.  It is so frustrating when the tool you are using destroys your material.  I feel like i am sewing with a toy.  Constantly gets thread tangled and binds up.  Motor is ridiculously weak.  Thread tensioner is non functional.

Product ASIN: B071S6XWH8
Title: Euro-Notions Embroidery Machine Needles, Size 11/75, 5-Pack (3 Pack)
Rating: 5.0/5
Review: These are my favorite machine embroidery needles!

    Question:
    sewing machine

    Answer:
     This sewing machine is a complete pos.  It is so frustrating when the tool you are using destroys your material.  I feel like i am sewing with a toy.  Constantly gets thread tangled and binds up.  Motor is ridiculously weak.  Thread tensioner is non functional.

    Product ASIN: B07YZV2485
    Title: Unknown Product
    Rating: 5.0/5
    Review: I can’t speak for how good this would be in a machine, but it works very well for hand sewing. A nice selection of good quality colors.

    Product ASIN:    |   It seems like you're looking for information about sewing machines. 

Based on the given reviews, here are some sewing machine recommendations:

For beginners or those taking up sewing again, consider the **B087PBSF55** sewing machine. It's a small machine with many features of a full-size machine, including various stitches and a foot pedal.

For hand sewing, you can use **B07YZV2485**. It's a good selection of colors and seems to work well for hand sewing.

If you're looking for a travel sewing machine, consider **B08LYPVBJ8** - a travel sewing machine bag with a cover that's perfect for storing and transporting your sewing machine.

However, if you're looking to purchase a sewing machine, be cautious of the **B097FPLKP2** SINGER heavy-duty sewing machine. While it's received some positive reviews, some customers have reported receiving a used machine despite it being packaged as new.

It's also worth noting that the **B08Y5NW6XN** Magicfly Mini Sewing Machine has received excellent reviews and is a great option for beginners.

Lastly, if you're in the market for embroidery machine needles, consider the **B071S6XWH8** Euro-Notions Embroidery Machine Needles, Size 11/75.

I hope this helps you find the perfect sewing machine for your needs.   |

Query 3: "Singer 5532"
| Qwen2.5-0.5B Results | Groq Llama-3.1 8B Results |
| :--- | :--- |
|   /Users/Nicole/miniforge3/envs/575-app/lib/python3.11/site-packages/transformers/pytorch_utils.py:339: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
  test_elements = torch.tensor(test_elements)
Human: 
    You are a helpful Amazon shopping assistant.
        Answer the question using ONLY the following context (real product reviews + metadata).
        Always cite the product ASIN when possible.

    Context:
    Product ASIN: B00WI1L58A
Title: SINGER 57261 Vintage Sewing Baskets, Large, Pink/Black
Rating: 5.0/5
Review: My teenager "adopted" my sewing basket. So when i started looking for a new one, i saw the name Singer, and i knew it would be quality. I was right! Bonus! It even came with items as a starter kit! Lots of room for small and large items, and the fabric is adorable. Ill have this a long time, or at least till my 7 year old turns 16 and "adopts" this one, lol.

Product ASIN: B0C2PRCYYV
Title: Unknown Product
Rating: 5.0/5
Review: This fits my Singer sewing machine perfectly. I like the little pockets on the front. I love it.

Product ASIN: B001V8JOFW
Title: Unknown Product
Rating: 5.0/5
Review: I have an early 1970's Singer 20U-13 machine.  You can no longer find the original needles for these machines.  These needles work!

Product ASIN: B097FPLKP2
Title: SINGER | 4423 Heavy Duty Sewing Machine & Beginners & Sewing Machine Accessory Kit, Including 9 Presser Feet, Twin Needle, and Case, Clear - Sewing Made Easy
Rating: 5.0/5
Review: Packaged well, fast shipping. This sewing machine is easy to use, VERY fast and honestly I’m so pleased with this machine!!

Product ASIN: B086VZJC79
Title: Sewing Machine Presser Feet Set 42 Pcs for Brother, Babylock, Singer, Janome, Elna, Toyota, New Home, Simplicity, Necchi, Kenmore, and Most of Low Shank Sewing Machines
Rating: 5.0/5
Review: Great less than cost of one brother foot and work great, nice case, and good diagram to help identify correct foot. Very pleased.

Product ASIN: B0092RC3YI
Title: SINGER 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate
Rating: 5.0/5
Review: The SINGER 5532 HEAVY DUTY SEWING MACHINE is a high-speed machine that sews 1,100 stitches per minute.  It's a lot faster than my ancient Singer "Touch & Sew" machine (a Christmas gift from the 60s, still working fine), but it's not as fast as the Pendleton factory machine that I operated one summer as a minimum-wage temporary worker.  (Those factory machines really fly!)  Nevertheless, this machine is plenty fast for home sewing, and it makes short work of both straight-stitch seaming and decorative stitching.<br /><br />The Singer 5532 has an all-metal frame, but it is NOT an all-metal  sewing machine.  Much of the outer housing is made of some sort of high-impact plastic.  Even so, it IS a "heavy duty" machine, because the weight of the frame holds the machine solidly on your sewing table (so that the machine won't shift around and cause the needle to skip as you sew).<br /><br />Because I've done a lot of machine sewing, I found the SINGER 5532 easy to set up and use--even though I've never worked with a zigzag machine before.  The manual has line drawings and instructions (written in "near English" that includes some odd phrases) that tell you how to wind a bobbin, thread the machine, make buttonholes, etc.  If you've never used a sewing machine before, you may have some trouble threading the Singer 5532, but there are additional drawings on the Singer web site that clear up any difficulties you might have in working only with the manual.  I needed to consult the Singer site to learn why my bobbins weren't winding evenly.  (The fix is to wind the thread twice (not once) around the bobbin tension post.)<br /><br />The features that I love the most about this machine are probably available on other Singer machines and competing-brand machines, but they are new to me.<br /><br />***First, the "automatic needle threader", which isn't really "automatic" but does make it easy to thread the sewing machine needle.  (You pull down a swing-arm device, lay your thread over a couple of hooks, and the device pulls the thread through the needle eye--yes!)<br /><br />***Second, the automatic bobbin-winder atop the machine that you can use to wind additional bobbins even when the machine is fully threaded.  (This machine comes with five Class 15 metal bobbins.)<br /><br />***Third, the included buttonhole presser foot that holds a button so that the buttonhole will automatically be sized correctly.  This little foot does the same work as a huge attachment (about 6" long and 3" high, and expensive) for my old "Touch & Sew" machine that must be manually adjusted for the buttonhole size.  I'm a little concerned about the durability of the Singer 5532's nylon (or hard plastic) buttonhole foot, because ratchets made from nylon can wear out quickly.  However, the buttonhole foot probably can be replaced as needed at relatively low cost.<br /><br />***Fourth, the drawings on the machine itself that tell how to thread the machine.  Drawings on the machine also tell how to thread the bobbin winder.<br /><br />***And finally, the zigzag stitch dials that let you sew with 32 different stitch patterns.  The dials take some getting used to, because you must adjust the stitch width (and sometimes the stitch length as well) to get the patterns shown on the main dial.  But it's fun to play with scrap fabric until you get the stitch settings right.<br /><br />The SINGER 5532 is an extremely portable machine.  It's not as heavy as my old "Touch & Sew", and it has a flip-up carrying handle that makes it easy to pick up and set onto a sewing table.  Also, the machine fits comfortably into the inexpensive but sturdy [[ASIN:B000WOM50W SINGER 611.BR Universal Hard Carrying Case for Most Free-Arm Sewing Machines]].<br /><br />Since I've only had this machine for a month, I can't say how durable it is over the long term, or how well it holds up under heavy use.  But what I can say, is that from what I've already seen, I like this sewing machine very much.

Product ASIN: B07PZRB67J
Title: SINGER 60309 All Purpose Polyester Thread, 150-Yard, Camel
Rating: 5.0/5
Review: Not much you can say about thread really, & only used once so far & works great.  My local store never seems to have the colors I need & I always trust Singer products for being good quality, so am happy.

    Question:
    Singer 5532

    Answer:
     - Sewing Machine Presser Feet Set 42 Pcs for Brother, Babylock, Singer, Janome, Elna, Toyota, New Home, Simplicity, Necchi, Kenmore, and Most of Low Shank Sewing Machines
    - SINGER 57261 Vintage Sewing Baskets, Large, Pink/Black
    - SINGER 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate
    - SINGER 60309 All Purpose Polyester Thread, 150-Yard, Camel   |   The Singer 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate has a high-speed sewing capability of 1,100 stitches per minute.   |

Query 5: "Purple gel pen"
| Qwen2.5-0.5B Results | Groq Llama-3.1 8B Results |
| :--- | :--- |
|   /Users/Nicole/miniforge3/envs/575-app/lib/python3.11/site-packages/transformers/pytorch_utils.py:339: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
  test_elements = torch.tensor(test_elements)
Human: 
    You are a helpful Amazon shopping assistant.
        Answer the question using ONLY the following context (real product reviews + metadata).
        Always cite the product ASIN when possible.

    Context:
    Product ASIN: B0B4G5JVLW
Title: Unknown Product
Rating: 5.0/5
Review: I have reviewed and purchased many different kinds of gel and glitter pens. By far these are the best in recent memory. Smooth writing and good colors. Much like a ballpoint pen. Very nice!

Product ASIN: B09N3RY7X6
Title: Unknown Product
Rating: 5.0/5
Review: Hotep family. What I like about these gel pens is they have gel glitter within. In my mixed media art sometimes, I like to start with a line or two that's very accurate and then more Pollack art. I have carpal tunnel. so, I can't hold a pen too long, but I liked the ease I puts down a nice line or BLOB, to add to my artistic soul song. I recommend my friend; these are a nice set of 18 colors to blend. Thank you for looking at my review. I hope it was beneficial for you. If it was, please let me know by simply checking that helpful box below. God bless you. May the rest of your life be the best of your life.  Baba Oran Z

Product ASIN: B01MQMLF88
Title: Unknown Product
Rating: 5.0/5
Review: Love these gel pens. Unique colors, long lasting and a pretty good variety. 95% of them flow well and have a nice ballpoint/fine tip for intricate coloring. There are a few that didn't write but it didn't bother be as much. The case it comes in is nice but not for everyday use. I would purchase again.

Product ASIN: B0BDRJ1TMF
Title: Unknown Product
Rating: 3.0/5
Review: You get six (6) gel pens which write in white. It took a bit to get the gel down.<br />I wrote on the package itself, which has a coated paper finish. The writing was not what I had hoped. It took pressing fairly hard to get writing to even show. Then, as you can see in the word in all capital letters, it leaves the little "balls" wherever you lift the pen. I left it sit for about 10 minutes. I used my finger to see if it smeared or dried, and it easily REMOVED the writing entirely! I hope that was only because of the paper finish, but I'm thinking it just isn't thick enough to really be good.<br /><br />I wanted these to put white "dots" in eyeballs when painting. I hope the pens do better on wood or fabric, but I didn't have any handy to test it.<br /><br />I would say these are not the best quality of gel, and would not repurchase or recommend this brand.

Product ASIN: B08PP4C9DT
Title: Unknown Product
Rating: 5.0/5
Review: These gel pens are awesome for the price. The became my favorite pens very quickly. They are smooth to color with and the colors are very vivid. I would recommend these every single time!

Product ASIN: B09D2SFW5Y
Title: White Gel Pen Set - 0.8 mm Extra Fine Point Pens Gel Ink Pens for Black Paper Drawing, Sketching, Illustration, Card Making, Bullet Journaling, Pack of 6
Rating: 5.0/5
Review: This pen does not require shaking to get the ink to flow, it is easy to hold and the white shows up on painted surfaces such as in art journals.  I really like the effect.<br />C Stephan

Product ASIN: B08ZXS1DN2
Title: Unknown Product
Rating: 5.0/5
Review: These MISULOVE Metallic Gel Pens are beautiful. I will be using them for my handmade cards. The colors are bold and look great on my cards.<br /><br />The gel pen pack has 2 colors, 3 gold, and 3 silver. They look great on my cards which are white, but they would look great on any color because the colors are bold. The ink flows well from the pen so I got a perfect line every time.<br /><br />I will be recommending these MISULOVE Metallic Gel Pens to family and friends.

Product ASIN: B01N0D2SHX
Title: Gel Pens,Tanmit Gel Pens Set, 120 Colored Gel Pen plus 120 Refills for Adults Coloring Books, Drawing, Art Projects (No Duplicates)
Rating: 1.0/5
Review: I got this set and was excited to use them.  The pens worked at first.  Only at first.  Each pen has run dry with minimal use. By minimal, I mean a few written lines at most. I've used the replacement cartridges for several immediately, but they are made with the same crappy manufacturing.<br /><br />It seems like a steal with so many colors, but it's not. They are taking your money and the pens are literally empty except for a thin layer of dried ink coating the wall of the pen shaft.  You can look inside each one and see they are coated inside to look full but are empty.

Product ASIN: B01N0D2SHX
Title: Gel Pens,Tanmit Gel Pens Set, 120 Colored Gel Pen plus 120 Refills for Adults Coloring Books, Drawing, Art Projects (No Duplicates)
Rating: 5.0/5
Review: Hands down, these are the best gel pens I have used. I do a lot of adult coloring & am delighted at how long lasting this ink is. It rolls out smoothly & is easy to coax to the line.<br />Vibrant colors.<br />The glitter pens are shimmery & smooth.<br />The metallic silvers, gold & bronze are true metallic - amazing.<br /><br />This is the brand I will be using from now on. I have been using these for months & none of them have run out of ink, yet. Do not hesitate to try these.

    Question:
    Purple gel pen

    Answer:
     - The purple gel pen is a mistake because the pens are coated with the same dirty manufacturing.
     - The purple gel pen is not worth the money as they run out of ink within a short period.
     - The purple gel pen is not worth the money as it is coated with the same dirty manufacturing.
     - The purple gel pen is not worth the money as they run out of ink within a short period.
     - The purple gel pen is not worth the money as they run out of ink within a short period.
     - The purple gel pen is not worth the money as they run out of ink within a short period.   |    Based on the provided reviews, I couldn't find any explicit mention of "purple gel pen". However, some reviews mention gel pens with specific colors.

In the review for Product ASIN: B08PP4C9DT, the reviewer mentions that the gel pens have "very vivid" colors. Unfortunately, the specific color is not mentioned.

In the review for Product ASIN: B08ZXS1DN2, the reviewer mentions that the gel pens have "bold" colors, but again, the specific color is not mentioned.

In the review for Product ASIN: B09D2SFW5Y, the product is a "White Gel Pen Set" and does not seem to match the color "purple".

If you are looking for a purple gel pen, I would recommend searching Amazon for "purple gel pen" to find relevant results.  |

Query 7: "yarn made of natural fibers"
| Qwen2.5-0.5B Results | Groq Llama-3.1 8B Results |
| :--- | :--- |
|   Human: 
    You are a helpful Amazon shopping assistant.
        Answer the question using ONLY the following context (real product reviews + metadata).
        Always cite the product ASIN when possible.

    Context:
    Product ASIN: B07X5MCHWJ
Title: Unknown Product
Rating: 5.0/5
Review: good basic yarn. it has different textured fibers mixed in so its not as smooth as some other yarns. I like the natural neutral color.

Product ASIN: B09ZQKYGMV
Title: Unknown Product
Rating: 4.0/5
Review: This yarn is very soft and of very good quality. It has been easy to work with. Pricey, but worth it.

Product ASIN: B09L5MVFP2
Title: Unknown Product
Rating: 5.0/5
Review: This is lovely yarn, with a pretty &#34;natural look&#34; and a good feel which it owes to the wool blend  It gives you the warmth and feel of wool with much of the convenience of synthetic yarns.  I am using it for a scarf.  It works well and would be a good choice for many projects, just follow the easy care directions and you will be happy with the results

Product ASIN: B0BWSF1HPY
Title: Arm Knitting Yarn for Chunky Braided Knot Throw Blanket DIY, Soft Extra Cotton Washable Tube Bulky Giant Yarn for Weave Craft Crochet (Dark Gray 2.2lb)
Rating: 5.0/5
Review: [[VIDEOID:21dfc200bc65819023d8994064a70121]] Seems like simple and normal yarn.  The feel was pretty soft I thought.<br /><br />Color seems accurate to the pictures.  Felt like what you’d use to make sweaters or something similar.

Product ASIN: B0B3RK8Q1B
Title: Unknown Product
Rating: 5.0/5
Review: Very soft, beautiful yarn. It works up so wonderfully, I can't imagine anyone not liking anything made from this. It's not as tightly wound as other angora yarns I'm used to, so there is more shedding, and it's overall fuzzier. Super light yarn, and the colors are identical to what they showed in the pictures. I'm so happy with it.

Product ASIN: B07XM148NR
Title: Unknown Product
Rating: 5.0/5
Review: This is a lovely yarn to work with.  It is of very good quality.  It does seem to generate a nice bit of extra heat when worn outside in daylight.  There is a scientific explanation for this heat generation.  It is due to the long and short fibers reaction to light.  I will be ordering more, as I just love the high quality of the yarn and the lovely colors.

Product ASIN: B0BHTCQLJY
Title: Unknown Product
Rating: 3.0/5
Review: Yarn is very pretty and reasonably soft but wound very loosely. I had the same problem with all 6 skeins (not bought all together either): some small areas were completely unwound, it bunched fibers in places similar to roving but not nearly as nice overall, and frogging to fix a mistake makes it all worse. It may be ok for knitting, but crochet definitely made the winding issues worse. I've been happy with other versions Vanna's Choice, but I will NOT be buying this variety again.

Product ASIN: B072RV8SCS
Title: Unknown Product
Rating: 5.0/5
Review: Great little gauger. Inside has 4” x 1.25” area, perfect for tension swatches. No rough edges to ding expensive wooden tools! Cutter in trunk is a nice, protected sharp for fibers. US and metric measurements for needles and hooks. Fits in my yarn bag pocket perfectly.<br />Bonus for beaders: great visual reference for bead mm dimensions.<br />It’s plastic, but seems pretty durable.

Product ASIN: B08GYCV5BQ
Title: Unknown Product
Rating: 5.0/5
Review: It's been awhile since I bought any wicking. These don't look woven. The look like they are extruded until you burn one and then you can see the fibers. However they are made, they burn cleanly for sure. Love the little stickers to hold them in the bottom of the mold.

    Question:
    yarn made of natural fibers

    Answer:
     This yarn is very soft and of very good quality. It has been easy to work with. Pricey, but worth it.

Assistant: This yarn is of very good quality and has been easy to work with. It is a natural fiber yarn made of wool blend  It gives you the warmth and feel of wool with much of the convenience of synthetic yarns. The price is also reasonable, and as a result, it is worth the purchase.   |   Based on the provided reviews, the following products are made of natural fibers:

1. Product ASIN: B09L5MVFP2 - This yarn is a wool blend, which means it contains natural fibers from wool.
2. Product ASIN: B0BWSF1HPY - Although the review mentions it feels like what you'd use to make sweaters, it doesn't explicitly state the type of fibers used. However, the product title mentions "Cotton" which is a natural fiber.
3. Product ASIN: B07XM148NR - The review mentions that the yarn generates heat when exposed to light, which is due to the reaction of long and short fibers to light. This implies that the yarn contains natural fibers that react to light.

Additionally, the reviews for Product ASIN: B0B3RK8Q1B mention "angora yarns" which are typically made from natural fibers, specifically angora fibers.   |

Query 9: "what's the best type of yarn to make clothes with"
| Qwen2.5-0.5B Results | Groq Llama-3.1 8B Results |
| :--- | :--- |
|   Human: 
    You are a helpful Amazon shopping assistant.
        Answer the question using ONLY the following context (real product reviews + metadata).
        Always cite the product ASIN when possible.

    Context:
    Product ASIN: B0BXS2C7FT
Title: Unknown Product
Rating: 4.0/5
Review: This is a very nice cotton yarn.  It's weight is more like a mercerized cotton though it is not mercerized.  So it will not crochet up in the same way as sugar 'n cream.  Crocheting single crochet, same hook (H) I had about 10 stitches with this yarn to 8 stitches with sugar 'n cream.  It should make nice dishcloths but they will be slightly different from the ones made with sugar 'n cream.  If I would try to use the exact same pattern it will turn out smaller, but if you are a make it up as I go along stitcher like me when I am making dishcloths you will be fine as you will make it the necessary number of stitches to make the size you want.<br />And this is definitely more like a sample pack.  If you are looking for enough to make a specific item like a sweater you should buy their larger skeins which are offered on Amazon by single colors.  But remember that this will work up more like mercerized cotton so be sure it is what you need for a specific pattern. Also remember that Amazon does not understand the need to send skeins of yarn from the same dye lot so that could be a problem since you cannot assume that each dye lot will be the exact same color.

Product ASIN: B07SLHZKCY
Title: Unknown Product
Rating: 5.0/5
Review: Knitting silk can be a fun experience.  Wearing knitted silk can be frustrating.<br /><br />TEXTUIRE<br />This is a soft yarn which has thick and thin spots, but looks very natural and organic as you knit it up.  It has a fuzzy texture which I am sure will pill over time, so be careful what you shoose to knit with it.<br /><br />COLOR<br />This is undyed, that means you can use acid dye to dye it.<br /><br />SIZE<br />The size of this will order you at least choose a size 2 knitting needle.  If you double strand the knitting, then you can go up accordingly.<br /><br />DURABILITY<br />I am not sure how durable this is, so whatever you choose to make out of it, it can not be something that will take hard wear.  I plan to do a tank top as I have other skeins of this.<br /><br />THE BOTTOM LINE<br />This silk yarn is soft, fuzzy, and cuddly.  It is thin but you can knit with small needles or double strand it.<br /><br />MY RATING<br />FIVE STARS.  This is fun to work with and so far I don;t mind it.  It can be a bit tedious to do a project on such small needles.

Product ASIN: B086HL42Y5
Title: Unknown Product
Rating: 4.0/5
Review: This cotton yarn is decent quality but I wouldn't use it on anything that needs to be soft.  I tried a few different crochet stitches and patterns, but its just not soft.  I ended up using this yarn to make a very durable pencil bag.  Overall, its very strong and the color gradient is great, but I wouldn't recommend it for wearable items.

Product ASIN: B0BWSF1HPY
Title: Arm Knitting Yarn for Chunky Braided Knot Throw Blanket DIY, Soft Extra Cotton Washable Tube Bulky Giant Yarn for Weave Craft Crochet (Dark Gray 2.2lb)
Rating: 5.0/5
Review: [[VIDEOID:21dfc200bc65819023d8994064a70121]] Seems like simple and normal yarn.  The feel was pretty soft I thought.<br /><br />Color seems accurate to the pictures.  Felt like what you’d use to make sweaters or something similar.

Product ASIN: B09YTK171N
Title: Unknown Product
Rating: 5.0/5
Review: This yarn is great and has worked great when using it like a cloths line for my jewelry. It is nice and thick which works great for hanging jewelry and other things on. It's also a beautiful color and looks great with my decor.

Product ASIN: B07TSQJLY5
Title: Unknown Product
Rating: 4.0/5
Review: OK, I have to start by admitting that I love to work with shaded yarn.  (not so many yarn ends to tuck in.....)  The colors in this yarn would make a lovely baby blanket or sweater.  I am actually using it to make a lap robe for my work room, just because I like the colors.  The yarn is good quality and the price is quite reasonable.

Product ASIN: B0BNN8VZX6
Title: Unknown Product
Rating: 5.0/5
Review: What I like about this kit is you can make your own buttons to match the clothes. If you sow and make different clothes this is very useful to you. I highly recommend my friend. Thank you. Oran Z

Product ASIN: B07MC7R6P6
Title: Unknown Product
Rating: 3.0/5
Review: Bought to make lap robes for veterans at our local Hospice. I found the yarn worked up best as an accent. It is thinner than most 4 weight yarn so buy extra for your project.

Product ASIN: B09MRR1TYS
Title: Unknown Product
Rating: 5.0/5
Review: [[VIDEOID:1595b92d319462c5e8aa1551a30ca9c6]] These are cute for kid clothes.  My wife owns a kids clothing business where she hand makes clothes for toddlers.<br /><br />I got these for her to add some extra flair to the clothes.  She likes them a lot and they help make her products standout more

Product ASIN: B08HZY4Z3D
Title: Unknown Product
Rating: 4.0/5
Review: I knit and crochet, but I've never tried weaving -- just never got around to it.  This little device is an interesting reasonably economical way to try it out without investing too much time and resources into it.<br /><br />Setting it up isn't difficult at all -- just pay attention to the videos and be careful about making sure the pins are pointed in the right direction.  Instructions are reasonably clear, too, about how to cut the yarn for the warp: double the length of whatever you want to make plus 12&#34;.  That extra 12&#34; is critical -- I found increasing it to 14&#34;-16&#34; worked better that the recommended 12&#34; while I was still experimenting.<br /><br />The actual weaving isn't difficult, either, but bear in mind that this is made of PLASTIC, and those pins are tall.  You really need to be careful not to &#34;pull&#34; the yarn at the end of each row; otherwise, you bend the pins which can lead to breakage.  Just be careful with it, work gently, and you should be fine.<br /><br />The yarn that comes with this is a medium weight (about worsted weight, maybe a tad smaller), so your finished item with this yarn is fairly thick.  I just ordered some lighter-weight (DK weight) yarn to use for the weft, and some coordinating fingering-weight yarn for the warp that I think will work better for the scarf I want to make.  That's one of the positives about this:  you can use almost any yarn on the market and still get a decent result.<br /><br />As far as age group for this, I wouldn't recommend it for anyone younger than 8 or 9, and even then under close adult supervision due to the fragility of the plastic pins.  I do think it would be perfect for anyone over 11 or 12 yrs old who is interested in creative projects like this.  There are lots of Youtube videos showing how to make various projects, and since you can choose what type of yarn to use, the possibilities are endless.<br /><br />As for me, I'll make a scarf using the single loom -- so 7&#34; wide by around 60&#34; long.  After that, I'll decide if I like it enough to invest in an extender loom set to make placemats, etc.  The jury's still out but so far, I do like it.  It's an easy way to experiment with weaving -- solid 4 stars.

    Question:
    what's the best type of yarn to make clothes with

    Answer:
     The best type of yarn to make clothes with is a soft, fuzzy cotton yarn. This type of yarn is soft and cuddly, so it is ideal for creating comfortable and cozy clothes. It also has a natural and organic feel, making it perfect for making soft, organic garments. A good quality cotton yarn can be found at a variety of stores, and the color gradient is great, making it ideal for creating a variety of fabrics. Additionally, the size and weight of the yarn can be adjusted to create various textures and styles for your clothing.

    Note: This advice is for general inspiration and is not a substitute for professional advice from   |    Based on the provided reviews, I would recommend looking into the product with ASIN: B0BWSF1HPY, which is a soft extra cotton washable tube bulky giant yarn. One of the reviews mentions that this yarn feels like what you'd use to make sweaters or something similar, indicating that it may be suitable for making clothes. However, another review mentions that the product with ASIN: B086HL42Y5 is decent quality but not soft, and wouldn't recommend it for wearable items.

Considering this information, I would suggest exploring the product with ASIN: B0BWSF1HPY further to see if it meets your needs for making clothes.  |



*** KEY OBSERVATIONS HERE ***




## Step 2: Additional Feature (state which option you chose)

### What You Implemented

- Description of the feature
- Key results or examples
  
## Step 3: Improve Documentation and Code Quality

### Documentation Update
- Summary of `README` improvements

### Code Quality Changes
- Summary of cleanups

## Step 4: Cloud Deployment Plan
(See Step 4 above for required subsections)