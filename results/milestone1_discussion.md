# Milestone 1 Qualitative Evaluation:

## Sample Queries and Comparison of Results:
### Query 1: "sewing machine"
Results of BM25:
```text
#1 | BM25 Score: 6.371
Product: Magicfly Mini Sewing Machine for Beginner, Dual Speed Portable Sewing Machine Machine with Extension Table, Light, Sewing Kit for Household, Travel
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Have not used yet, but directions look ok to switch thread.
--------------------------------------------------
#2 | BM25 Score: 6.232
Product: SINGER 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  The SINGER 5532 HEAVY DUTY SEWING MACHINE is a high-speed machine that sews 1,100 stitches per minute.  It's a lot faster than my ancient Singer "Touch & Sew" machine (a Christmas gift from the 60s,...
--------------------------------------------------
#3 | BM25 Score: 6.169
Product: SINGER | 4423 Heavy Duty Sewing Machine & Beginners & Sewing Machine Accessory Kit, Including 9 Presser Feet, Twin Needle, and Case, Clear - Sewing Made Easy
Rating:  ⭐⭐ (2/5)
Review:  I was looking for something that could sew jeans and such heavy fabrics or multiple layered fabrics. Thought this one would be great as the name itself says heavy duty. Machine is super easy to...
--------------------------------------------------
#4 | BM25 Score: 6.056
Product: Euro-Notions Embroidery Machine Needles, Size 11/75, 5-Pack (3 Pack)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  These are my favorite machine embroidery needles!
--------------------------------------------------
#5 | BM25 Score: 5.804
Product: Casulo 5 in 1 Heat Press Machine Combo, 360-Degree Rotation Tshirt Press Machine Digital Sublimation, Multifunctional Heat Press 12x15 Inch Heat Transfer for T-Shirts Mug Hats Plate Cap
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  THE GOOD:<br />--------------<br />* Heavy duty, super high quality machine.<br />* Spacious 12x15 platform.<br />* Big and bright LCD control panel.<br />* 360 degree "swing away" design gives you...
--------------------------------------------------
```

Results of Semantic Search:
```text
#1 | L2 Distance: 0.517
Product: SINGER | 4423 Heavy Duty Sewing Machine & Beginners & Sewing Machine Accessory Kit, Including 9 Presser Feet, Twin Needle, and Case, Clear - Sewing Made Easy
Rating:  ⭐⭐ (2/5)
Review:  I was looking for something that could sew jeans and such heavy fabrics or multiple layered fabrics. Thought this one would be great as the name itself says heavy duty. Machine is super easy to...
--------------------------------------------------
#2 | L2 Distance: 0.579
Product: Janome 2212 Sewing Machine Includes Exclusive Bonus Bundle
Rating:  ⭐ (1/5)
Review:  This sewing machine is a complete pos.  It is so frustrating when the tool you are using destroys your material.  I feel like i am sewing with a toy.  Constantly gets thread tangled and binds up. ...
--------------------------------------------------
#3 | L2 Distance: 0.600
Product: EverSewn Sparrow 30 Sewing Machine : Computer-Controlled, 310 Stitch Patterns, 2 Full Alphabets-Perfect for The Creative Sewer
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I'm seriously in love with this little machine! After using a Kenmore for over 20 years and fighting nearly every time with threading issues, and jammed needles, this is a breeze. I love all the...
--------------------------------------------------
#4 | L2 Distance: 0.617
Product: EverSewn Sparrow 30 Sewing Machine : Computer-Controlled, 310 Stitch Patterns, 2 Full Alphabets-Perfect for The Creative Sewer
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Although I did not purchase my machine from Amazon, but wanted to put in a review.  I love the Sparrow 30.. I've sewn on it for a week and it's great.  I've played with a few different features on...
--------------------------------------------------
#5 | L2 Distance: 0.618
Product: SINGER 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  The SINGER 5532 HEAVY DUTY SEWING MACHINE is a high-speed machine that sews 1,100 stitches per minute.  It's a lot faster than my ancient Singer "Touch & Sew" machine (a Christmas gift from the 60s,...
--------------------------------------------------
```

Discussion of Query 1: "sewing machine"
This is one of the simplest queries we tested, which we expected would work well for both BM25 and semantic search methods, as this phrase would likely appear in both the title and review text, and likely has a well-defined embedding. As we can see in the results above, both search methods successfully returned sewing machines in their top results. The BM25 search seems to have returned higher ranked sewing machines, while the semantic search method prioritizes smallest L2 distance over highest rating. 


### Query 2: "acrylic paint"
Results of BM25:
==================================================
#1 | BM25 Score: 7.611
Product: Shuttle Art Acrylic Paint, 18 Colors Acrylic Paint Bottle Set (240ml/8.12oz), Rich Pigmented Acrylic Paints, Bulk Painting Supplies for Artists, Beginners and Kids on Rocks Crafts Canvas Wood Ceramic
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Great Paints, Great Price and my Artist Daughter is thrilled with them.
--------------------------------------------------
#2 | BM25 Score: 7.478
Product: Betem 12 Colors Dual Tip Acrylic Paint Pens Markers, Acrylic Paint Pens for Wood, Canvas, Stone, Rock Painting, Glass, Ceramic Surfaces, DIY Crafts Making (12 DUAL TIP PAINT PENS)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  These are awesome. Pretty colors that are vibrant. They glide right on.
--------------------------------------------------
#3 | BM25 Score: 6.887
Product: FolkArt Home Décor acrylic paint, 2oz, Antique Wax 2 Fl Oz
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Use this paint all the time
--------------------------------------------------
#4 | BM25 Score: 6.788
Product: Nicpro 32 Colors Outdoor Acrylic Paint Bulk with Brush and Sponge, Knife, Non-Toxic Paint for Multi-surface Rock, Wood, Fabric, Leather, Crafts, Canvas, Shoes and Wall Painting
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Nicpro 32 Colors Outdoor Acrylic Paint Bulk with Brush and Sponge, Knife, Non-Toxic Paint for Multi-Surface Rock,  You can use these paints indoors also. Just for the fun of it I am going to leave...
--------------------------------------------------
#5 | BM25 Score: 6.451
Product: Codirom Wet Palette Paint Palette for Acrylic Paints Palette for Miniatures Pigment Palette Model Paint Keeps Your Paint Wet for Longer Wet Palette (Green)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  When you have that perfect color mixed, you can make more of it and store it in this container. It helps your acrylic last longer by not giving it the air it needs to dry out. Thank you for reading...
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 0.739
Product: Nicpro 32 Colors Outdoor Acrylic Paint Bulk with Brush and Sponge, Knife, Non-Toxic Paint for Multi-surface Rock, Wood, Fabric, Leather, Crafts, Canvas, Shoes and Wall Painting
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I have plenty of acrylics.  One of the things I don't have, however, is acrylic that is designed to be used outdoors.  This kit is just that.<br /><br />HOW DOES THIS COME?<br />This set comes in a...
--------------------------------------------------
#2 | L2 Distance: 0.765
Product: ARTEZA Acrylic Paint, Set of 60 Colors, 0.74 oz/22 ml Tubes, includes 5 Metallic Colors, Rich Pigments, Non-Fading, Non-Toxic Paints for Artist & Hobby Painters, Art Supplies for Painting
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  I used this today to do some monoprinting on coasters. It is a good smooth and creamy paint. Vibrant colors and a good selection.  I deducted one star because the bottles are hard to get open and...
--------------------------------------------------
#3 | L2 Distance: 0.781
Product: ARTEZA Acrylic Paint, Set of 60 Colors, 0.74 oz/22 ml Tubes, includes 5 Metallic Colors, Rich Pigments, Non-Fading, Non-Toxic Paints for Artist & Hobby Painters, Art Supplies for Painting
Rating:  ⭐⭐⭐ (3/5)
Review:  The set comes with 20, 2 fl oz bottles of acrylic paints. The colors are vivivd, have a matte finish, are quick drying, and blendable. The colors as they show on the box, dont exactly match the...
--------------------------------------------------
#4 | L2 Distance: 0.790
Product: ARTEZA Acrylic Paint, Set of 60 Colors, 0.74 oz/22 ml Tubes, includes 5 Metallic Colors, Rich Pigments, Non-Fading, Non-Toxic Paints for Artist & Hobby Painters, Art Supplies for Painting
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Great paint for canvases or crafts. Mixes well to  use in paint pouring. Very saturated colors.
--------------------------------------------------
#5 | L2 Distance: 0.802
Product: Droaful Acrylic Paint Pens Markers Set-12 Color Paint Pens for Rock Painting, Stone, Ceramic, Glass, Wood, Fabric, Canvas, Porcelain, Metal,Non-Toxic and No Odor
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  [[VIDEOID:4b61b5307061a0b09025f531b8ca331]] Nice paint pens - very easy to use.<br /><br />The finish is nice.  You can make very pretty art with them<br /><br />Design is pretty cool.  So many nice...
--------------------------------------------------

### Query 3: "Singer 5532"
Results of BM25:
==================================================
#1 | BM25 Score: 14.257
Product: SINGER 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  The SINGER 5532 HEAVY DUTY SEWING MACHINE is a high-speed machine that sews 1,100 stitches per minute.  It's a lot faster than my ancient Singer "Touch & Sew" machine (a Christmas gift from the 60s,...
--------------------------------------------------
#2 | BM25 Score: 7.332
Product: SINGER 57261 Vintage Sewing Baskets, Large, Pink/Black
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  My teenager "adopted" my sewing basket. So when i started looking for a new one, i saw the name Singer, and i knew it would be quality. I was right! Bonus! It even came with items as a starter kit!...
--------------------------------------------------
#3 | BM25 Score: 6.331
Product: Distinctive 1-4” (Quarter Inch) Quilting Sewing Machine Presser Foot - Fits All Low Shank Snap-On Singer*, Brother, Babylock, Euro-Pro, Janome, Kenmore, White, Juki, New Home, Simplicity, Elna + More!
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I’ve used it twice on two thick fleece pieces sewn together  and had no problems.
--------------------------------------------------
#4 | BM25 Score: 4.071
Product: YRDQNCraft 3pcs Sewing Machine Presser Foot Set-Adjustable Guide Sewing Machine Presser Foot,Zig Zag Snap On Foot Presser Foot, Border Guide Sewing Machine Presser Foot Fits Singer, Brother
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I use a Sophia 2 from Babylock. These machines are very similar to Brother machines, so I was not sure these feet would fit, they do. I really wanted to try the wide foot with the grid. Some fabrics...
--------------------------------------------------
#5 | BM25 Score: 3.425
Product: SINGER | 4423 Heavy Duty Sewing Machine & Beginners & Sewing Machine Accessory Kit, Including 9 Presser Feet, Twin Needle, and Case, Clear - Sewing Made Easy
Rating:  ⭐⭐ (2/5)
Review:  I was looking for something that could sew jeans and such heavy fabrics or multiple layered fabrics. Thought this one would be great as the name itself says heavy duty. Machine is super easy to...
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 1.113
Product: SINGER 57261 Vintage Sewing Baskets, Large, Pink/Black
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  My teenager "adopted" my sewing basket. So when i started looking for a new one, i saw the name Singer, and i knew it would be quality. I was right! Bonus! It even came with items as a starter kit!...
--------------------------------------------------
#2 | L2 Distance: 1.333
Product: SINGER 5532 Heavy Duty Extra-High Sewing Speed Portable Sewing Machine with Metal Frame and Stainless Steel Bedplate
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  The SINGER 5532 HEAVY DUTY SEWING MACHINE is a high-speed machine that sews 1,100 stitches per minute.  It's a lot faster than my ancient Singer "Touch & Sew" machine (a Christmas gift from the 60s,...
--------------------------------------------------
#3 | L2 Distance: 1.414
Product: Distinctive 1-4” (Quarter Inch) Quilting Sewing Machine Presser Foot - Fits All Low Shank Snap-On Singer*, Brother, Babylock, Euro-Pro, Janome, Kenmore, White, Juki, New Home, Simplicity, Elna + More!
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I’ve used it twice on two thick fleece pieces sewn together  and had no problems.
--------------------------------------------------
#4 | L2 Distance: 1.506
Product: YRDQNCraft 3pcs Sewing Machine Presser Foot Set-Adjustable Guide Sewing Machine Presser Foot,Zig Zag Snap On Foot Presser Foot, Border Guide Sewing Machine Presser Foot Fits Singer, Brother
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I use a Sophia 2 from Babylock. These machines are very similar to Brother machines, so I was not sure these feet would fit, they do. I really wanted to try the wide foot with the grid. Some fabrics...
--------------------------------------------------
#5 | L2 Distance: 1.506
Product: SINGER | 4423 Heavy Duty Sewing Machine & Beginners & Sewing Machine Accessory Kit, Including 9 Presser Feet, Twin Needle, and Case, Clear - Sewing Made Easy
Rating:  ⭐⭐ (2/5)
Review:  I was looking for something that could sew jeans and such heavy fabrics or multiple layered fabrics. Thought this one would be great as the name itself says heavy duty. Machine is super easy to...
--------------------------------------------------

### Query 4: "Animal stickers"
Results of BM25 Search:
==================================================
#1 | BM25 Score: 11.866
Product: Lilihan Diamond Dots Kits 5D DIY Diamond Painting Kits for Kids Cartoon Animal Stickers Paint with Diamonds Kits DIY Arts Crafts
Rating:  ⭐ (1/5)
Review:  Cheap price but cheap quality.  Not worth it.
--------------------------------------------------
#2 | BM25 Score: 7.460
Product: 120 Pieces Vintage Scrapbooking Stickers DIY Journaling Scrapbook Adhesive Washi Paper Stamp Stickers Antique Retro Natural Collection Stickers Diary Journal Embellishment Supplies (Artsy Style)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Great pack for the price. Would purchase again if needed
--------------------------------------------------
#3 | BM25 Score: 7.346
Product: Aromoty Flower Gold foil Holographic Stickers Set( 120 pieces with 3 Themes)-Resin Transparent Waterproof Stickers,Butterfly,Vintage Daily Planner Stickers for Scrapbook Junk Bullet Journals, Laptop,Water bottles Decor for kids adults (Flower B- Warm)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Lots of pretty shiny stickers and great quality, variety.
--------------------------------------------------
#4 | BM25 Score: 6.781
Product: Knaid Butterfly Dragonfly Insects Stickers Set (240 Pieces) - PET Transparent Waterproof Decorative Decals for Scrapbook DIY Crafts Album Bullet Journal Planner Water Bottles Phone Cases Laptops
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Beautiful stickers very sheer and great results
--------------------------------------------------
#5 | BM25 Score: 6.649
Product: Hot Off The Press Dazzles Stickers 6"X9" 3 Sheets-Black Swirls, Flourishes & Borders
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I love these stickers! They look like stamped/heat embossed designs, but they're peel-and-stick.<br /><br />I use these for cards, and they're super easy to use.  One tip: use tweezers to help align...
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 0.808
Product: Knaid Butterfly Dragonfly Insects Stickers Set (240 Pieces) - PET Transparent Waterproof Decorative Decals for Scrapbook DIY Crafts Album Bullet Journal Planner Water Bottles Phone Cases Laptops
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Beautiful stickers very sheer and great results
--------------------------------------------------
#2 | L2 Distance: 0.846
Product: Aromoty Flower Gold foil Holographic Stickers Set( 120 pieces with 3 Themes)-Resin Transparent Waterproof Stickers,Butterfly,Vintage Daily Planner Stickers for Scrapbook Junk Bullet Journals, Laptop,Water bottles Decor for kids adults (Flower B- Warm)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Lots of pretty shiny stickers and great quality, variety.
--------------------------------------------------
#3 | L2 Distance: 0.878
Product: Hot Off The Press Dazzles Stickers 6"X9" 3 Sheets-Black Swirls, Flourishes & Borders
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I love these stickers! They look like stamped/heat embossed designs, but they're peel-and-stick.<br /><br />I use these for cards, and they're super easy to use.  One tip: use tweezers to help align...
--------------------------------------------------
#4 | L2 Distance: 0.933
Product: 120 Pieces Vintage Scrapbooking Stickers DIY Journaling Scrapbook Adhesive Washi Paper Stamp Stickers Antique Retro Natural Collection Stickers Diary Journal Embellishment Supplies (Artsy Style)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Great pack for the price. Would purchase again if needed
--------------------------------------------------
#5 | L2 Distance: 0.940
Product: Jolee's Boutique Cooking Dimensional Stickers
Rating:  ⭐ (1/5)
Review:  My daughter recently moved out on her own and I’m making her a recipe scrapbook.  I was so excited to get these as an addition to the scrapbook, but my excitement was short lived. These are super...
--------------------------------------------------

### Query 5: "Purple gel pen"
Results of BM25:
==================================================
#1 | L2 Distance: 0.821
Product: Gel Pens,Tanmit Gel Pens Set, 120 Colored Gel Pen plus 120 Refills for Adults Coloring Books, Drawing, Art Projects (No Duplicates)
Rating:  ⭐ (1/5)
Review:  I got this set and was excited to use them.  The pens worked at first.  Only at first.  Each pen has run dry with minimal use. By minimal, I mean a few written lines at most. I've used the...
--------------------------------------------------
#2 | L2 Distance: 0.842
Product: Gel Pens,Tanmit Gel Pens Set, 120 Colored Gel Pen plus 120 Refills for Adults Coloring Books, Drawing, Art Projects (No Duplicates)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Hands down, these are the best gel pens I have used. I do a lot of adult coloring & am delighted at how long lasting this ink is. It rolls out smoothly & is easy to coax to the line.<br />Vibrant...
--------------------------------------------------
#3 | L2 Distance: 0.850
Product: White Gel Pen Set - 0.8 mm Extra Fine Point Pens Gel Ink Pens for Black Paper Drawing, Sketching, Illustration, Card Making, Bullet Journaling, Pack of 6
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  This pen does not require shaking to get the ink to flow, it is easy to hold and the white shows up on painted surfaces such as in art journals.  I really like the effect.<br />C Stephan
--------------------------------------------------
#4 | L2 Distance: 0.882
Product: Diamonday 5D Diamond Art Painting Pen Holder Silicone Tool Stand Accessories (Pink Holder)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  When doing diamond paintings, it helps to have a pen that has some grip to it.  This is a great upgrade from the usual thin tube pens.<br /><br />HOW THIS COMES<br />This comes in a little plastic...
--------------------------------------------------
#5 | L2 Distance: 0.933
Product: Shuttle Art 18 Pack Micro-line Pens, Waterproof Archival Ink, 11 Colors in 0.3MM Felt Tip & 7 Blacks in Sizes 0.15MM to 0.5MM Multiliner For Journaling Technical Illustrating Drawing Manga Zentangle
Rating:  ⭐⭐⭐ (3/5)
Review:  It's what I get for not paying attention, but this is not the brand I thought I was ordering. I thought to exchange the pens when I realized, but I did need the pens and the assortment was good, so I...
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 0.821
Product: Gel Pens,Tanmit Gel Pens Set, 120 Colored Gel Pen plus 120 Refills for Adults Coloring Books, Drawing, Art Projects (No Duplicates)
Rating:  ⭐ (1/5)
Review:  I got this set and was excited to use them.  The pens worked at first.  Only at first.  Each pen has run dry with minimal use. By minimal, I mean a few written lines at most. I've used the...
--------------------------------------------------
#2 | L2 Distance: 0.842
Product: Gel Pens,Tanmit Gel Pens Set, 120 Colored Gel Pen plus 120 Refills for Adults Coloring Books, Drawing, Art Projects (No Duplicates)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Hands down, these are the best gel pens I have used. I do a lot of adult coloring & am delighted at how long lasting this ink is. It rolls out smoothly & is easy to coax to the line.<br />Vibrant...
--------------------------------------------------
#3 | L2 Distance: 0.850
Product: White Gel Pen Set - 0.8 mm Extra Fine Point Pens Gel Ink Pens for Black Paper Drawing, Sketching, Illustration, Card Making, Bullet Journaling, Pack of 6
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  This pen does not require shaking to get the ink to flow, it is easy to hold and the white shows up on painted surfaces such as in art journals.  I really like the effect.<br />C Stephan
--------------------------------------------------
#4 | L2 Distance: 0.882
Product: Diamonday 5D Diamond Art Painting Pen Holder Silicone Tool Stand Accessories (Pink Holder)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  When doing diamond paintings, it helps to have a pen that has some grip to it.  This is a great upgrade from the usual thin tube pens.<br /><br />HOW THIS COMES<br />This comes in a little plastic...
--------------------------------------------------
#5 | L2 Distance: 0.933
Product: Shuttle Art 18 Pack Micro-line Pens, Waterproof Archival Ink, 11 Colors in 0.3MM Felt Tip & 7 Blacks in Sizes 0.15MM to 0.5MM Multiliner For Journaling Technical Illustrating Drawing Manga Zentangle
Rating:  ⭐⭐⭐ (3/5)
Review:  It's what I get for not paying attention, but this is not the brand I thought I was ordering. I thought to exchange the pens when I realized, but I did need the pens and the assortment was good, so I...
--------------------------------------------------

### Query 6: "cute embroidery patterns"
Results of BM25:
==================================================
#1 | BM25 Score: 12.982
Product: Bonroy 4 Sets Embroidery Kit for Beginners,Embroidery Kit for Art Craft Handy Sewing Include Embroidery Clothes with Pattern,Embroidery Hoops, Instructions,Color Threads Needle Kit (Multi 4)
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This is a really cute kit with four different floral patterns and two hoops (if you want to give the finished embroideries away with hoops, you'll need to purchase two more on your own). I'd give...
--------------------------------------------------
#2 | BM25 Score: 6.773
Product: Embroidery Beginner Kits,5 Pack Embroidery Starter Kit Set Embroidered Stitching Pendants Hand Sewing Necklace Earrings Pendant Necklace DIY Charm Necklace with Needle Thread,Handmade Embroidery Gift
Rating:  ⭐ (1/5)
Review:  The instructions are literally in a foreign language.
--------------------------------------------------
#3 | BM25 Score: 6.654
Product: BIHRTC 4.5 Inch Embroidery Scissors Vintage and 3.6 Inch Stork Scissors Sharp Stainless Steel Dressmaker Small Shears 2 Pack Scissors for Craft Household Needlework Rainbow Scissors
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  The rainbow iridescence on this stainless steel pair of scissors is beyond magical! I do love a whimsical craft supply, and these little birds are both cute AND reliable! The scissored hinge...
--------------------------------------------------
#4 | BM25 Score: 6.618
Product: Embroidery Scissors Kits Include 2 Pairs Vintage Scissors, European Style Sewing Scissors with Sewing Needle Case, Thimble, Threader, Complete Sewing Kit for Embroidery, Needlework (Red Copper)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Bought this for my wife as embroidery gift and she loves it. Wonderful gift and made.
--------------------------------------------------
#5 | BM25 Score: 6.534
Product: Euro-Notions Embroidery Machine Needles, Size 11/75, 5-Pack (3 Pack)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  These are my favorite machine embroidery needles!
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 0.665
Product: Stitcher's Revolution Iron-On Transfer Pattern for Embroidery, Around The World Landmarks
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  These iron on transfers take me back to childhood when I was first learning to stitch.  They are easy to apply and work up quickly.  They make it easy to personalize all sorts of cloth items,...
--------------------------------------------------
#2 | L2 Distance: 0.694
Product: Bonroy 4 Sets Embroidery Kit for Beginners,Embroidery Kit for Art Craft Handy Sewing Include Embroidery Clothes with Pattern,Embroidery Hoops, Instructions,Color Threads Needle Kit (Multi 4)
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This is a really cute kit with four different floral patterns and two hoops (if you want to give the finished embroideries away with hoops, you'll need to purchase two more on your own). I'd give...
--------------------------------------------------
#3 | L2 Distance: 0.719
Product: Embroidery Kit for Beginners Funny - 4 Sets Cross Stitch Kits Beginner with 4 Embroidery Patterns/Hoops Kits/Embroidery Thread and Tools for Beginners Adults Kids (Deer, Flamingo, Alpaca, Bird)
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This is a nice kit, but my wife and kids were excited to try something new and actually found this difficult to pick up. It claims to be for beginners, however without any stitch experience it wasn't...
--------------------------------------------------
#4 | L2 Distance: 0.719
Product: Simplicity Sewing Pattern 2499 Men's Costumes, BB (L-XL)
Rating:  ⭐⭐⭐ (3/5)
Review:  Pattern has a lot of different options which is neat. On the pattern I received, the ink was faded and extremely hard to read in most places.
--------------------------------------------------
#5 | L2 Distance: 0.754
Product: Shuanshuo Black Series Floral Cotton Fabric Textile Quilting Patchwork Fabric Fat Quarter Bundles Fabric for Scrapbooking Cloth Sewing DIY Crafts Pillows 50X50cm 7pcs/lot
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  November mix of patterns
--------------------------------------------------

### Query 7: "yarn made of natural fibers"
Results of BM25:
==================================================
#1 | BM25 Score: 9.364
Product: Knit Picks Dishie Worsted Weight 100% Cotton Yarn Purple - 100 g (Mulberry)
Rating:  ⭐⭐⭐ (3/5)
Review:  I generally buy an organic DK weight cotton yarn for all my projects, but was looking for something with a little more bulk that was at least natural if not organic. I found this and liked the color...
--------------------------------------------------
#2 | BM25 Score: 9.239
Product: YUYOYE Super Soft Fluffy Fur Yarn for Crochet and Knitting, Faux Fur Thick & Quick Bulky Yarn (07-Aqua Grey,6Pack)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  One of the softest yarns I've ever felt. It's fur effect is very good looking, and I have made some incredible amigurumi from this and I just can't imagine them looking any better with any other...
--------------------------------------------------
#3 | BM25 Score: 8.908
Product: Bernat Baby Blanket Cloud Nine Yarn - 2 Pack of 300g/10.5oz - Polyester - 6 Super Bulky - 220 Yards - Knitting/Crochet
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I just made knit blanket for my daughter she love it
--------------------------------------------------
#4 | BM25 Score: 7.998
Product: (1 Skein) 24/7 Cotton® Yarn, Ecru
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  This is a wonderful cotton yarn.  High quality, easy to work with, long lasting, versatile.<br />It is mercerized so it will not be like sugar 'n cream if that is what you are looking for.  It leans...
--------------------------------------------------
#5 | BM25 Score: 7.947
Product: (3 Pack) Lion Brand Yarn Vanna's Choice Yarn, Fisherman
Rating:  ⭐⭐⭐ (3/5)
Review:  it's alright for american yarn. i don't understand why european yarn is so beautiful and all we can get in america is the same type of yarn for many years...there is no progress.
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 0.812
Product: Arm Knitting Yarn for Chunky Braided Knot Throw Blanket DIY, Soft Extra Cotton Washable Tube Bulky Giant Yarn for Weave Craft Crochet (Dark Gray 2.2lb)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  [[VIDEOID:21dfc200bc65819023d8994064a70121]] Seems like simple and normal yarn.  The feel was pretty soft I thought.<br /><br />Color seems accurate to the pictures.  Felt like what you’d use to make...
--------------------------------------------------
#2 | L2 Distance: 0.903
Product: Bernat Handicrafter Cotton Yarn, Gauge 4 Medium Worsted, Salt/Pepper
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This cotton yarn is a decent option for making dish cloths and pot holders, but I would not recommend it for anything wearable. I like the colors, but they are a little lighter than the photo looks. ...
--------------------------------------------------
#3 | L2 Distance: 0.974
Product: Crafted By Catherine Velvet Chain Yarn - 3 Pack, Red, Gauge 6 Super Bulky
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Very beautiful yarn with an oddly dense/firm feel. Looks good worked up and was a nice, easy yarn to work with. A couple of my skeins had knots, one didn't. Overall, a good yarn and I would recommend...
--------------------------------------------------
#4 | L2 Distance: 1.012
Product: Bernat Softee Baby Yarn, 5 oz, Antique White, 1 Ball
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Very soft, smooth and light weight. There were no fuzz, fading, or shrinkage after washing and drying.  I'm impressed! I've attached a picture of my blanket after 2 washes.
--------------------------------------------------
#5 | L2 Distance: 1.020
Product: Gisimo 100% Inner Mongolian Cashmere Yarn Luxurious Hand Knitting Yarn Home Necessity for DIY Crafts
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Best quality cashmere I've ever had. It doesn't shed and hasn't pilled yet either. Wonderfully soft and such nice colors. But of course, as always, I wish there were more colors. This worked up...
--------------------------------------------------

### Query 8: "best paint for wood"
Results of BM25:
==================================================
#1 | BM25 Score: 10.062
Product: Unfinished Wood Ornaments, PETUOL DIY 32pcs 4x3in Creative Irregular Blank Wood Natural Slices for DIY Crafts, Painting, Wood Burning, Writing, Photo Props, Coasters and Home Decorations
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  These little blanks are the best. I love making little decorative signs with vinyl. These are just perfect for that. Lightweight and they don't need sanding. Might try some wood burning on a few too...
--------------------------------------------------
#2 | BM25 Score: 9.110
Product: Metallic Marker Paint Pens Sets for Wood: AKARUED Glitter Color Pen Kit for Drawing, Art Rock Painting, Fabric, Black Paper, Wine, Ceramic, Craft, Coloring, Card Making for Adults, Kids, Set of 12
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Loving these paint pens so much. They are so beautiful and work great for coloring clay, rocks, and even wood. They are super juicy with the ink flowing wonderfully from these. They all have a...
--------------------------------------------------
#3 | BM25 Score: 8.511
Product: Betem 12 Colors Dual Tip Acrylic Paint Pens Markers, Acrylic Paint Pens for Wood, Canvas, Stone, Rock Painting, Glass, Ceramic Surfaces, DIY Crafts Making (12 DUAL TIP PAINT PENS)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  These are awesome. Pretty colors that are vibrant. They glide right on.
--------------------------------------------------
#4 | BM25 Score: 8.254
Product: Nicpro 32 Colors Outdoor Acrylic Paint Bulk with Brush and Sponge, Knife, Non-Toxic Paint for Multi-surface Rock, Wood, Fabric, Leather, Crafts, Canvas, Shoes and Wall Painting
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Nicpro 32 Colors Outdoor Acrylic Paint Bulk with Brush and Sponge, Knife, Non-Toxic Paint for Multi-Surface Rock,  You can use these paints indoors also. Just for the fun of it I am going to leave...
--------------------------------------------------
#5 | BM25 Score: 8.157
Product: Shuttle Art Acrylic Paint, 18 Colors Acrylic Paint Bottle Set (240ml/8.12oz), Rich Pigmented Acrylic Paints, Bulk Painting Supplies for Artists, Beginners and Kids on Rocks Crafts Canvas Wood Ceramic
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Great Paints, Great Price and my Artist Daughter is thrilled with them.
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 1.048
Product: Moshify Pebeo Vitrea 160 Glass Paint - Transparent Colour Glossy and Brilliant - Made in France - DIY Craft Paint for Stained Glass and More - Set of 8 Colors Bundled Application Brushes
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I have used glass paints in the past, but none were ever permanent. I like the Pebeo Vitrea 160 Glass Paint set with the Moshify brushes because this is a good variety of colors to start. I'm...
--------------------------------------------------
#2 | L2 Distance: 1.053
Product: DIY Paint by Numbers, Canvas Oil Painting Kit for Adults, 16" W x 20" L Drawing Paintwork with Paintbrushes, Acrylic Pigment
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Arrived quickly and packed well. Although the box has several errors (spelling, grammer, etc) it doesn't take away from the quality of the actual product. Everything you need comes in the pack...
--------------------------------------------------
#3 | L2 Distance: 1.064
Product: Metallic Marker Paint Pens Sets for Wood: AKARUED Glitter Color Pen Kit for Drawing, Art Rock Painting, Fabric, Black Paper, Wine, Ceramic, Craft, Coloring, Card Making for Adults, Kids, Set of 12
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Loving these paint pens so much. They are so beautiful and work great for coloring clay, rocks, and even wood. They are super juicy with the ink flowing wonderfully from these. They all have a...
--------------------------------------------------
#4 | L2 Distance: 1.075
Product: FolkArt Home Décor acrylic paint, 2oz, Antique Wax 2 Fl Oz
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  Use this paint all the time
--------------------------------------------------
#5 | L2 Distance: 1.078
Product: White Paint Markers for Rocks Painting, Ceramic, Glass, Wood, Fabric, Canvas, Mugs, Cobblestone, Pumpkin Decorating Kit, DIY Craft Making Supplies. 8 Medium Tip Acrylic Water Based Paint Pens
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  White touches can make or break designs. On dark surfaces, pure whites can be hard to achieve. These white acrylic paint markers are the solution. Once activated (easy), the white acrylic paint flows...
--------------------------------------------------

### Query 9: "what's the best type of yarn to make clothes with"
Results of BM25:
==================================================
#1 | BM25 Score: 17.290
Product: YUYOYE Super Soft Fluffy Fur Yarn for Crochet and Knitting, Faux Fur Thick & Quick Bulky Yarn (07-Aqua Grey,6Pack)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  One of the softest yarns I've ever felt. It's fur effect is very good looking, and I have made some incredible amigurumi from this and I just can't imagine them looking any better with any other...
--------------------------------------------------
#2 | BM25 Score: 15.652
Product: Mary Maxim Scrub It Yarn, Plum
Rating:  ⭐⭐⭐ (3/5)
Review:  First, the good news.  The pattern for making a scrubby that comes with the yarn is accurate and easy to follow.  And, one skein really does make a scrubby, not large, but big enough to do the job. ...
--------------------------------------------------
#3 | BM25 Score: 15.571
Product: (1 Skein) 24/7 Cotton® Yarn, Ecru
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  This is a wonderful cotton yarn.  High quality, easy to work with, long lasting, versatile.<br />It is mercerized so it will not be like sugar 'n cream if that is what you are looking for.  It leans...
--------------------------------------------------
#4 | BM25 Score: 15.288
Product: (3 Pack) Lion Brand Yarn Vanna's Choice Yarn, Fisherman
Rating:  ⭐⭐⭐ (3/5)
Review:  it's alright for american yarn. i don't understand why european yarn is so beautiful and all we can get in america is the same type of yarn for many years...there is no progress.
--------------------------------------------------
#5 | BM25 Score: 15.183
Product: Zoid 3-in-1 Adjustable Utility Knife with Contoured Body and Trax-Grip for Safe and Easy Cutting, Functions as a Precision Utility Knife, Wire Stripper, and Carabiner, Box Cutter, Wire Cutter
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I selected this utility knife after having a good impression of another Zoid knife, which has proven to be one of the best utility knives I have ever used. I like this one too.<br /><br />There are a...
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 0.689
Product: Arm Knitting Yarn for Chunky Braided Knot Throw Blanket DIY, Soft Extra Cotton Washable Tube Bulky Giant Yarn for Weave Craft Crochet (Dark Gray 2.2lb)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  [[VIDEOID:21dfc200bc65819023d8994064a70121]] Seems like simple and normal yarn.  The feel was pretty soft I thought.<br /><br />Color seems accurate to the pictures.  Felt like what you’d use to make...
--------------------------------------------------
#2 | L2 Distance: 0.789
Product: Bernat Handicrafter Cotton Yarn, Gauge 4 Medium Worsted, Salt/Pepper
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This cotton yarn is a decent option for making dish cloths and pot holders, but I would not recommend it for anything wearable. I like the colors, but they are a little lighter than the photo looks. ...
--------------------------------------------------
#3 | L2 Distance: 0.841
Product: Lion Brand Yarn 5800-526 Martha Stewart Glitter Eyelash Yarn, Brownstone
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This pretty, sparkly eyelash yarn  adds a lovely, glamorous  look to to various projects.  The yarn has a touch of delicate pink, and also reflects sparkly rainbow colors.  I am just learning to work...
--------------------------------------------------
#4 | L2 Distance: 0.854
Product: Kona Cotton Capri, Fabric by the Yard
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  Kaufman Kona is always a nice quality of fabric.<br />I have a color chart of their items, and it is always exactly on without variances.<br /><br />Note that Kona is a relatively low-thread-count...
--------------------------------------------------
#5 | L2 Distance: 0.918
Product: Lion Brand Yarn Bonbons Yarn, Nature 8 x 28 yd/26 m
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I have found these Bonbons to be just wonderful for making motif projects and flower, etc accents.  Picture a scarf, a little bag, or even crochet jewelry in a rainbow of colors.  The Lion company...
--------------------------------------------------

### Query 10: "what is a good type of yarn for a beginner"
Results of BM25:
==================================================
#1 | BM25 Score: 20.107
Product: VGOODALL 5PCS Round Knitting Loom Set Circular Loom Set Hook Needles with 4 Skeins Acrylic Yarn for Hat Scarf Shawl Sweater Sock Pompom
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  A very good set of looms. Good construction.  I like the yarn selection which might be almost enough to make a small hat for practice. Instructions and needles included. A really good beginner kit.
--------------------------------------------------
#2 | BM25 Score: 18.471
Product: (3 Pack) Lion Brand Yarn Vanna's Choice Yarn, Fisherman
Rating:  ⭐⭐⭐ (3/5)
Review:  it's alright for american yarn. i don't understand why european yarn is so beautiful and all we can get in america is the same type of yarn for many years...there is no progress.
--------------------------------------------------
#3 | BM25 Score: 18.338
Product: (1 Skein) 24/7 Cotton® Yarn, Ecru
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  This is a wonderful cotton yarn.  High quality, easy to work with, long lasting, versatile.<br />It is mercerized so it will not be like sugar 'n cream if that is what you are looking for.  It leans...
--------------------------------------------------
#4 | BM25 Score: 17.518
Product: Ashford 10 in SampleIt Loom Stand
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  This loom is very easy to use and is quite versatile. it is suitable for both beginner and experienced weavers, who know how to take advantage of its features to achieve a variety of woven effects....
--------------------------------------------------
#5 | BM25 Score: 17.458
Product: YUYOYE Super Soft Fluffy Fur Yarn for Crochet and Knitting, Faux Fur Thick & Quick Bulky Yarn (07-Aqua Grey,6Pack)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  One of the softest yarns I've ever felt. It's fur effect is very good looking, and I have made some incredible amigurumi from this and I just can't imagine them looking any better with any other...
--------------------------------------------------

Results of Semantic Search:
==================================================
#1 | L2 Distance: 0.751
Product: Arm Knitting Yarn for Chunky Braided Knot Throw Blanket DIY, Soft Extra Cotton Washable Tube Bulky Giant Yarn for Weave Craft Crochet (Dark Gray 2.2lb)
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  [[VIDEOID:21dfc200bc65819023d8994064a70121]] Seems like simple and normal yarn.  The feel was pretty soft I thought.<br /><br />Color seems accurate to the pictures.  Felt like what you’d use to make...
--------------------------------------------------
#2 | L2 Distance: 0.887
Product: Lion Brand Yarn 5800-526 Martha Stewart Glitter Eyelash Yarn, Brownstone
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This pretty, sparkly eyelash yarn  adds a lovely, glamorous  look to to various projects.  The yarn has a touch of delicate pink, and also reflects sparkly rainbow colors.  I am just learning to work...
--------------------------------------------------
#3 | L2 Distance: 0.918
Product: Bernat Handicrafter Cotton Yarn, Gauge 4 Medium Worsted, Salt/Pepper
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This cotton yarn is a decent option for making dish cloths and pot holders, but I would not recommend it for anything wearable. I like the colors, but they are a little lighter than the photo looks. ...
--------------------------------------------------
#4 | L2 Distance: 0.952
Product: Lion Brand Yarn Bonbons Yarn, Nature 8 x 28 yd/26 m
Rating:  ⭐⭐⭐⭐⭐ (5/5)
Review:  I have found these Bonbons to be just wonderful for making motif projects and flower, etc accents.  Picture a scarf, a little bag, or even crochet jewelry in a rainbow of colors.  The Lion company...
--------------------------------------------------
#5 | L2 Distance: 1.005
Product: Embroidery Kit for Beginners Funny - 4 Sets Cross Stitch Kits Beginner with 4 Embroidery Patterns/Hoops Kits/Embroidery Thread and Tools for Beginners Adults Kids (Deer, Flamingo, Alpaca, Bird)
Rating:  ⭐⭐⭐⭐ (4/5)
Review:  This is a nice kit, but my wife and kids were excited to try something new and actually found this difficult to pick up. It claims to be for beginners, however without any stitch experience it wasn't...
--------------------------------------------------

