# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->
Off-campus housing in downtown San Jose is a significant challenge for students, particularly because Northeastern University's San Jose campus does not provide student housing. As a result, students must independently search for accommodation, a process that can be especially overwhelming for international students who are unfamiliar with the local housing market. A centralized platform that aggregates available housing options, along with verified reviews and insights from current or former tenants, would streamline the search process and help students make more informed housing decisions.

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

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

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 500 characters

**Overlap:** 75 characters

**Reasoning:** Each review is a self-contained opinion, so the review is my natural unit of meaning. In the corpus, the length of the reviews varies widely from ~135 characters (one line review) to ~1385 characters (long multi-topic reviews covering several complaints at once). A fixed-size splitter would cut these mid-sentences, so I will be using RecursiveCharacterTextSplitter.

My corpus is well structured and separates reviews with a blank line, so I split on blank lines first to isolate individual reviews, then apply the recursive splitter within each review. With a chunk size of **500 characters,** most reviews fall under the cap and stay as a single unit, while the few long multi-topic reviews are subdivided at natural boundaries, rather than arbitrary character counts.

I am using **75 character overlap (15% of chunk size)** so that when a long review is split, a context of the sentence carries across the boundary. Short reviews stay whole and are unaffected by overlap.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** I am planning to first use **all-MiniLM-L6-v2 via sentence-transformers.** If the retrieval quality is not good, I will try different embedding models.

**Top-k:** 5. Since, each embedding is approximately one review, we would be taking 5 relevant reviews to get related information.

**Production tradeoff reflection:** `all-MiniLM-L6-v2` is a strong default because it is small, runs locally with no API cost, and is fast enough to embed the whole corpus in seconds. But it has a 256-token input cap and is trained mostly on general English, which matters for this corpus. If I were deploying this for real students and cost were not a concern, I would weigh:

- **Accuracy on domain text:** Reviews use informal, opinion-heavy language ("nickel-and-dimed," "bait-and-switch," ESA/HUD references). A larger model like `all-mpnet-base-v2` or an API model such as OpenAI `text-embedding-3-large`, Voyage, or Cohere Embed would likely give better semantic matching on these nuanced complaints, improving which 5 reviews surface.
- **Multilingual support:** Several of my reviewers are international students (e.g., a UK student at 27 North), and future users may search in other languages. A multilingual model (e.g., `paraphrase-multilingual-mpnet-base-v2` or Cohere multilingual) would handle non-English queries better.
- **Context length:** Not a big concern here — my chunks are ≤500 characters, so MiniLM's 256-token window rarely truncates. A longer-context model would mainly help if I stopped chunking and embedded whole long reviews.
- **Latency vs. accuracy vs. privacy:** Local MiniLM is the lowest-latency, most private option. An API model adds per-query cost, network latency, and sends review text to a third party, but typically improves retrieval quality. For a small student tool I would stay local unless evaluation shows MiniLM is missing relevant reviews.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What do reviewers say about package delivery and the package fee at Miro San Jose? | There is a mandatory ~$25–$35/month package/delivery fee, yet packages are frequently delivered 1–2 days late or pile up at the front desk. Only one package concierge serves both towers, so deliveries stop when he is off, and several reviewers note theft risk because non-residents can enter the lobby. |
| 2 | How reliable are the elevators at 27 North, and how does management handle outages? | Elevators are frequently nonoperational — broken for 2+ months at a time, and by one resident's account roughly 10 of 36 months over three years. Management usually sends no notice or acknowledgement, it is a safety/access hazard (especially for disabled residents), and rent is still charged in full despite the missing amenity. |
| 3 | What problems do residents report with the parking system at Sparq? | Sparq uses a Klaus stacker parking system that breaks down often; one resident had to rent a car when it was down for days, and residents leaving stacker doors open blocks access. Reviews are mixed — a few call it safe and efficient, but several say it is hard to use and management is slow to fix it. |
| 4 | How close is The Grad to SJSU campus, and have residents noticed a change after the management switch? | The Grad is about a 5-minute walk to SJSU campus. Many reviewers say a newer management company (praised staff like Brandon and Matthew) improved the property, though some recent reviews report it declined again after another management change. Recurring complaints are broken elevators, hot water shut off without notice, and move-in/billing issues. |
| 5 | Is Sparq accommodating to pets and emotional support animals (ESAs)? | Mixed. One reviewer with a dog calls the building very pet-friendly, but another describes their ESA being mishandled: retroactive pet fees charged despite providing an ESA letter, the manager (Camisha) allegedly misstating AB 468/HUD rules, raising Fair Housing concerns and no follow-up from management or legal. |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1. **Polarized, contradictory reviews bias the answer.** Almost every apartment has both glowing 5-star reviews and scathing 1-star reviews (Miro and The Grad reviewers even accuse some 5-star reviews of being fake). If top-k retrieval happens to pull mostly positive *or* mostly negative chunks for a query, the generated answer will misrepresent the overall sentiment. I plan to retrieve k=5 and prompt the model to present both positive and negative points when they exist, and I'll watch for this skew during evaluation.

2. **Cross-apartment contamination / wrong source attribution.** Reviews frequently mention *other* properties by name — 27 North reviews compare to "the Grad" and "Sparta505," and Sparq/Sparta names are similar. A query about one apartment could retrieve a chunk that is actually comparing to or talking about a different building, causing the model to attribute a complaint to the wrong place. Tagging every chunk with its source apartment in metadata (from the `# Source:` header) and surfacing that source in the answer is my mitigation.

3. **Long multi-topic reviews split across chunk boundaries.** Some reviews are ~1,300+ characters covering several distinct complaints (fees + smoking + noise + management) in one block. My 500-char chunking can split a single complaint across two chunks, so retrieval might return only half the context for a specific question. The 75-char overlap reduces but does not eliminate this; I'll check for it in the failure-case analysis.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

```
┌──────────────────────────┐
│  1. Document Ingestion   │   10 .txt files in documents/
│                          │   (apartment reviews, one file per property,
│  Python file I/O         │    each with a "# Source:" / "# Address:" header)
└────────────┬─────────────┘
             │  raw review text + source metadata
             ▼
┌──────────────────────────┐
│  2. Chunking             │   split on blank lines → isolate each review,
│                          │   then RecursiveCharacterTextSplitter
│  langchain text splitter │   chunk_size=500 chars, overlap=75 chars
└────────────┬─────────────┘   each chunk keeps {source, address} metadata
             │  list of chunks
             ▼
┌──────────────────────────┐
│  3. Embedding +          │   embed each chunk → 384-dim vector
│     Vector Store         │   model: all-MiniLM-L6-v2
│                          │   store vectors + text + metadata
│  sentence-transformers   │   persistent collection
│  + ChromaDB              │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│  4. Retrieval            │   embed user query with same model,
│                          │   similarity search, top-k = 5 chunks
│  ChromaDB query          │   (returns text + source metadata)
└────────────┬─────────────┘
             │  query + 5 retrieved chunks
             ▼
┌──────────────────────────┐
│  5. Generation +         │   build grounded prompt (system prompt +
│     Interface            │   retrieved chunks as context), call LLM,
│                          │   show answer with sources to the user
│  Groq LLM + Gradio       │
│                          |
└──────────────────────────┘
```


---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

- _Tool:_ Claude (Claude Code).
- _Input I'll give it:_ My **Chunking Strategy** section (split on blank lines first, then RecursiveCharacterTextSplitter, chunk_size=500, overlap=75) plus the format of my `documents/*.txt` files (each starts with `# Source:` and `# Address:` lines, reviews separated by blank lines).
- _What I expect it to produce:_ A `load_documents()` function that reads every file in `documents/`, parses out the source/address header, and a `chunk_text()` function that returns chunks each tagged with `{source, address}` metadata.
- _How I'll verify:_ Print the total chunk count and spot-check several chunks — confirm short reviews stay whole, a long multi-topic review is split at natural boundaries, and every chunk carries the correct source apartment.

**Milestone 4 — Embedding and retrieval:**

- _Tool:_ Claude (Claude Code), referencing the official sentence-transformers / ChromaDB docs.
- _Input I'll give it:_ My **Retrieval Approach** section (embedding model `all-MiniLM-L6-v2`, top-k=5) and the chunk-with-metadata structure from Milestone 3.
- _What I expect it to produce:_ Code that embeds all chunks, stores vectors + text + metadata in a persistent ChromaDB collection, and a `retrieve(query, k=5)` function that embeds the query with the same model and returns the top 5 chunks with their source metadata.
- _How I'll verify:_ Run my 5 evaluation questions and inspect whether the retrieved chunks are actually relevant and attributed to the right apartment (checking for the cross-apartment contamination risk I flagged).

**Milestone 5 — Generation and interface:**

- _Tool:_ Claude (Claude Code) for the prompt + Groq integration and the Gradio.
- _Input I'll give it:_ My **Anticipated Challenges** (esp. polarized reviews and wrong-source attribution) so the system prompt is written to stay grounded, present both positive and negative points, cite the source apartment, and say "I don't know" when the retrieved reviews don't cover the question.
- _What I expect it to produce:_ A `generate_answer(query)` function that retrieves chunks, formats them into a grounded prompt for the Groq LLM, and a simple Gradio/Streamlit interface where a user types a question and sees the answer plus the source apartments it drew from.
- _How I'll verify:_ Run the 5 test questions end-to-end, confirm answers only use retrieved content, check that sources are surfaced, and test an out-of-scope question to confirm the model declines instead of hallucinating.
