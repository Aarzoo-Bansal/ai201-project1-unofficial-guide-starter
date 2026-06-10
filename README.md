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
| 8 | Modera San Pedro Square | Text File | Google Review: https://www.google.com/maps/place/Modera+San+Pedro+Square/@37.3352154,-121.8966746,17z/data=!4m8!3m7!1s0x808fcd94f600431b:0x35ed8a2bc87fba81!8m2!3d37.3352154!4d-121.8940997!9m1!1b1!16s%2Fg%2F11j0cxnghz?entry=ttu&g_ep=EgoyMDI2MDYwMy4xIKXMDSoASAFQAw%3D%3D <br><br> Apartments.com: https://www.apartments.com/modera-san-pedro-square-san-jose-ca/5m60lvp/#reviewsSection |
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

**Chunk size:** 500 characters

**Overlap:** 75 characters

**Reasoning:** Each review is a self-contained opinion, so the review is my natural unit of meaning. In the corpus, the length of the reviews varies widely from ~135 characters (one line review) to ~1385 characters (long multi-topic reviews covering several complaints at once). A fixed-size splitter would cut these mid-sentences, so I will be using RecursiveCharacterTextSplitter.

My corpus is well structured and separates reviews with a blank line, so I split on blank lines first to isolate individual reviews, then apply the recursive splitter within each review. With a chunk size of **500 characters,** most reviews fall under the cap and stay as a single unit, while the few long multi-topic reviews are subdivided at natural boundaries, rather than arbitrary character counts.

I am using **75 character overlap (15% of chunk size)** so that when a long review is split, a context of the sentence carries across the boundary. Short reviews stay whole and are unaffected by overlap.

**Final chunk count:** 337

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:** all-MiniLM-L6-v2

**Production tradeoff reflection:** `all-MiniLM-L6-v2` is a strong default because it is small, runs locally with no API cost, and is fast enough to embed the whole corpus in seconds. But it has a 256-token input cap and is trained mostly on general English, which matters for this corpus. If I were deploying this for real students and cost were not a concern, I would weigh:

- **Accuracy on domain text:** Reviews use informal, opinion-heavy language ("nickel-and-dimed," "bait-and-switch," ESA/HUD references). A larger model like `all-mpnet-base-v2` or an API model such as OpenAI `text-embedding-3-large`, Voyage, or Cohere Embed would likely give better semantic matching on these nuanced complaints, improving which 5 reviews surface.
- **Multilingual support:** Several of my reviewers are international students (e.g., a UK student at 27 North), and future users may search in other languages. A multilingual model (e.g., `paraphrase-multilingual-mpnet-base-v2` or Cohere multilingual) would handle non-English queries better.
- **Context length:** Not a big concern here — my chunks are ≤500 characters, so MiniLM's 256-token window rarely truncates. A longer-context model would mainly help if I stopped chunking and embedded whole long reviews.
- **Latency vs. accuracy vs. privacy:** Local MiniLM is the lowest-latency, most private option. An API model adds per-query cost, network latency, and sends review text to a third party, but typically improves retrieval quality. For a small student tool I would stay local unless evaluation shows MiniLM is missing relevant reviews.

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

Grounding is enforced at three points in the pipeline ([generate.py](generate.py)), not just by the prompt:

**1. System prompt grounding instruction.** Every request is sent with a system prompt whose first rule is a hard grounding constraint:

> *GROUNDING. Base every statement solely on the REVIEWS provided in the user message. Never use outside knowledge or invent details (fees, dates, names, policies). If the reviews do not contain the answer, say so plainly: "The reviews I have don't cover that." Do not guess.*
>
> *ATTRIBUTION. The reviews are about specific apartments. Attribute each point to the apartment it comes from (e.g., "At Sparq, reviewers say..."). If the question names an apartment, only use reviews whose source is that apartment; ignore reviews about other buildings even if they sound similar.*
>
> *BOTH SIDES. Reviews for the same building often conflict. When they do, present both the positive and the negative rather than collapsing to one verdict.*

The ATTRIBUTION and BOTH SIDES rules directly target the two risks named in `planning.md` (cross-building confusion and contradictory reviews). The model runs at **temperature 0.1** to keep it faithful to the source text rather than creative.

**2. Structural choices (context formatting).** Retrieved chunks are not dumped in as plain text — each is rendered as a numbered, source-labelled block: `[3] Apartment: 27 North (relevance 0.57)\n<review text>`. Tagging each block with its apartment is what makes correct attribution possible and lets the model recognize and discard chunks from the wrong building.

**3. Low-relevance filtering.** Before building the prompt, chunks below a cosine-similarity threshold (`MIN_SCORE = 0.15`) are dropped so the model is never tempted to answer from a barely-related review. If *nothing* clears retrieval, the system short-circuits and returns "The reviews I have don't cover that." without ever calling the LLM — so an out-of-scope question can't trigger a hallucination.

**How source attribution is surfaced in the response:** `generate_answer()` returns the distinct apartments behind the answer, and the Gradio UI ([app.py](app.py)) renders a **Sources** panel beneath every answer listing (a) the apartments cited and (b) each retrieved review snippet with its source and relevance score. The user can therefore see exactly which reviews — and which buildings — the answer was built from. An optional apartment dropdown also lets the user constrain retrieval to a single building via a ChromaDB metadata filter (`where={"source": ...}`).

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

Run with no source filter (top-k = 5), against the 5 questions from `planning.md`.

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | Package delivery & fee at Miro San Jose? | ~$25–35/mo package fee; packages 1–2 days late or pile up at the desk; one concierge for both towers (deliveries stop when he's off); theft risk from non-residents in the lobby. | Reported the $25–35/mo fee, 1–2 day delays, packages sitting at the desk, and one concierge serving both towers; also surfaced a positive 24/7-concierge review. Did **not** mention the theft/lobby-access risk. | Relevant (4/5 chunks from Miro; 1 from The James, unused) | Accurate (minor omission: theft risk) |
| 2 | Elevator reliability & outage handling at 27 North? | Broken 2+ months at a time, ~10 of 36 months over 3 years; little/no notice; safety hazard esp. for disabled residents; rent charged in full. | Correctly reported elevators broken 2+ months, both down, down ≥5 days (Jan 2025), management "blows you off," AC-leak-bucket anecdote. **Missed** the "10 of 36 months" stat and "rent charged in full." | Partially relevant (only 2/5 chunks from 27 North; 3 from Avalon/The Grad) | Partially accurate (correct but incomplete) |
| 3 | Parking system problems at Sparq? | Klaus stacker breaks often; one resident rented a car when it was down for days; open stacker doors block access; mixed (some call it safe/efficient, others slow to fix). | Reported the stacker as a "constant headache," days-long shutdown, open doors blocking access, "parking is a mess"/dismissive management, plus a "safe indoor parking 5/5" positive. Missed the "Klaus" brand name and the rental-car detail. | Relevant (3/5 chunks from Sparq; Taft/Avalon chunks unused) | Accurate |
| 4 | Grad's proximity to SJSU & change after management switch? | ~5-min walk to SJSU; new management praised and improved the property, but some recent reviews say it declined again after another switch; recurring elevator/hot-water/billing complaints. | Reported the 5-min walk and that new management "improved tremendously"; correctly flagged that some retrieved chunks were 27 North, not The Grad. **Missed** the later decline and recurring complaints — said there were "only positive" management comments. | Partially relevant (2/5 chunks from 27 North contamination) | Partially accurate (missed the decline nuance) |
| 5 | Is Sparq accommodating to pets/ESAs? | Mixed: one dog owner calls it very pet-friendly; another's ESA was mishandled — retroactive pet fees despite an ESA letter, PM allegedly misstating AB 468/HUD rules, Fair Housing concerns, no follow-up. | Captured the negative ESA case well (retroactive fees, ESA letter, HUD Fair Housing) and noted others praise the PM. **Missed** the "very pet-friendly" dog-owner review and the specific AB 468 citation. | Relevant (5/5 chunks from Sparq) but low scores (0.38–0.50) | Partially accurate (got the ESA complaint, missed the positive side) |

**Summary:** 2/5 Accurate, 3/5 Partially accurate, 0/5 Inaccurate. No hallucinations — every claim traced to a retrieved review, and the model correctly refused or flagged cross-building chunks. The recurring weakness is **recall, not precision**: when the answer was incomplete (Q2, Q4, Q5) it was because a relevant review didn't make the top-5, usually displaced by a semantically-similar chunk from another building.

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

**Question that failed:** Q2 — "How reliable are the elevators at 27 North, and how does management handle outages?"

**What the system returned:** A correct but **incomplete** answer. It reported that the elevators were broken 2+ months, that both were down, that they were out ≥5 days in Jan 2025, and that management "blows you off" (plus the AC-leak-bucket anecdote). It **omitted** two key facts from the expected answer: that one resident logged the elevators as inactive ~10 of 36 months over three years, and that rent is still charged in full despite the missing amenity. Importantly, the answer was *not wrong* — it did not hallucinate or misattribute; it simply didn't have those facts available.

**Root cause (tied to a specific pipeline stage): retrieval, cross-building contamination.** Inspecting the top-5 chunks, **only 2 of the 5 were actually from 27 North.** The other three were a near-identical elevator complaint from *Avalon at Cahill Park* (score 0.622) and two from *The Grad San Jose* (0.612, 0.568) — both of which out-scored the genuine 27 North chunks (0.570). This is exactly the "cross-building confusion" risk flagged in `planning.md`: every building in the corpus complains about broken elevators and unresponsive management in the same language, so `all-MiniLM-L6-v2` ranks those chunks as highly similar regardless of which building they describe. Because three of the five retrieval slots were consumed by other buildings, the 27 North reviews containing the "10 of 36 months" and "rent charged in full" details never made the top-5 — so the generator, correctly refusing to use the off-building chunks, had no way to include them. The failure is **recall at the retrieval stage**, not a generation error (the system prompt's attribution rule actually worked — it kept the wrong-building details *out* of the answer).

**What you would change to fix it:** The system already supports the fix — passing `source="27 North - Student Housing Apartments"` applies a ChromaDB metadata filter (`where={"source": ...}`) so all 5 slots go to genuine 27 North reviews. Re-running Q2 with that filter recovers the missing "~10 months of 3 years" detail. To make this automatic rather than manual, I would: (1) **detect the apartment name in the query** (the questions almost always name a building) and apply the source filter automatically; and/or (2) **over-fetch then re-rank** — retrieve top-15, then keep the top-5 *after* filtering to the target building, so contaminating chunks don't crowd out relevant ones. A larger, domain-tuned embedding model (e.g. `all-mpnet-base-v2`) would also widen the score gap between the right building and look-alike complaints, but the metadata filter is the cheaper, more reliable fix here.

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
