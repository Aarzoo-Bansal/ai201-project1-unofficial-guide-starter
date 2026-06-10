# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

Off-campus housing in downtown San Jose is a significant challenge for students, particularly because Northeastern University's San Jose campus does not provide student housing. As a result, students must independently search for accommodation, a process that can be especially overwhelming for international students who are unfamiliar with the local housing market. A centralized platform that aggregates available housing options, along with verified reviews and insights from current or former tenants, would streamline the search process and help students make more informed housing decisions.
<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | Miro San Jose Apartments | Text File | Google Review: https://maps.google.com/?cid=12605233222488082840  <br><br> Apartments.com: https://www.apartments.com/miro-san-jose-ca/bsvyvv8/#reviewsSection|
| 2 | One South Market | Text File | Reddit: https://www.reddit.com/r/SanJose/comments/llfzkq/to_residents_of_one_south_market_what_are_the/ <br><br> ApartmentRatings: https://www.apartmentratings.com/ca/san-jose/one-south-market_9199332346275157470/#ratingsReviews <br><br> Google Rviews: https://www.google.com/maps/place/One+South+Market+Apartments/data=!4m2!3m1!1s0x808fcca36c9f5fcf:0xb994b20eac0de073 |
| 3 | Avalon at Cahil Park | Text File | Google Reviews: https://www.google.com/maps/place/Avalon+at+Cahill+Park/@37.330938,-121.9078553,17z/data=!4m8!3m7!1s0x808fcb58d58e0cd3:0x61bbcbce262f82ae!8m2!3d37.330938!4d-121.9052804!9m1!1b1!16s%2Fg%2F1tghdclk?entry=ttu&g_ep=EgoyMDI2MDYwMy4xIKXMDSoASAFQAw%3D%3D <br><br> Reddit: https://www.reddit.com/r/SanJose/comments/10xz1lk/avalon_on_alameda_vs_cahill_park/ <br><br> ApartmentRating: https://www.apartmentratings.com/ca/san-jose/avalon-at-cahill-park_408292777895126/?page=2#ratingsReviews|
| 4 | 27 North - Student Housing Apartment | Text File | Reddit: https://www.reddit.com/r/SJSU/comments/1awmty8/thoughts_on_27_north/ <br><br> Google Reviews: https://www.google.com/maps/place/27+North+-+Student+Housing+Apartments/data=!4m2!3m1!1s0x0:0x901b56921e53dda3?sa=X&ved=1t:2428&ictx=111&cshid=1781042218037963|
| 5 | Sparq | Text File | Google Reviews: https://maps.google.com/?cid=17704956175015793473 |
| 6 | The Grad San Jose | Text File | Yelp: https://www.yelp.com/biz/the-grad-san-jose-3#reviews <br><br> Google Reviews: https://www.google.com/maps/place/The+Grad+San+Jose/@37.3323077,-121.8877265,17z/data=!3m1!4b1!4m6!3m5!1s0x808fcd48239fd593:0xae227f992f24823!8m2!3d37.3323077!4d-121.8851516!16s%2Fg%2F11fphqcz8y?entry=ttu&g_ep=EgoyMDI2MDYwMy4xIKXMDSoASAFQAw%3D%3D |
| 7 | The James Apartments | Text File | Yelp: https://www.yelp.com/biz/the-james-san-jose#reviews <br><br> Gogle Reviews: https://maps.google.com/?cid=13141732054850696562 |
| 8 | Modera San Pedro Square | Text File | Google Review:  <br><br> Apartments.com: https://www.apartments.com/modera-san-pedro-square-san-jose-ca/5m60lvp/#reviewsSection |
| 9 | The Taft Apartments | Text File | Google Reviews: https://www.google.com/maps/place/The+Taft+Apartments/@37.3285317,-121.8887645,17z/data=!4m8!3m7!1s0x808fcd9f030c3f71:0x1d02e00586d6c29b!8m2!3d37.3285317!4d-121.8861896!9m1!1b1!16s%2Fg%2F11t9qkk9_0?entry=ttu&g_ep=EgoyMDI2MDYwMy4xIKXMDSoASAFQAw%3D%3D <br><br> |
| 10 | The Ryden Apartments | Text File | Google Reviews: https://www.google.com/maps/place/The+Ryden+Apartments/@37.3277531,-121.8899607,17z/data=!4m8!3m7!1s0x808fcd5e82e9f6d3:0x6a473fb694a45e98!8m2!3d37.3277531!4d-121.8873858!9m1!1b1!16s%2Fg%2F11hdrpnxj8?entry=ttu&g_ep=EgoyMDI2MDYwMy4xIKXMDSoASAFQAw%3D%3D |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:**

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
