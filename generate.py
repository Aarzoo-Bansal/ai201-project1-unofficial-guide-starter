"""Milestone 5 — Grounded generation.

Full pipeline (this module covers stage 5's generation half):

    1. Document Ingestion   ingest.load_documents()      [ingest.py]
    2. Chunking             ingest.chunk_text()          [ingest.py]
    3. Embedding + Store     SentenceTransformer + Chroma [retrieval.py]
    4. Retrieval            retrieval.retrieve()         [retrieval.py]
    5. Generation           Groq LLM, grounded prompt    <-- THIS FILE
       + Interface          Gradio                       [app.py]

Per planning.md (AI Tool Plan, Milestone 5) the system prompt is written to
directly address the Anticipated Challenges:

  * Stay grounded — answer ONLY from the retrieved reviews, never invent facts.
  * Polarized reviews — when reviews disagree, present BOTH sides rather than
    collapsing to a single sentiment.
  * Wrong-source attribution — cite the apartment each claim comes from, so a
    cross-building chunk can't masquerade as the asked-about building.
  * Out-of-scope — say the reviews don't cover it instead of hallucinating.

Usage:
    python generate.py "your question"          # answer one question
    python generate.py --source Sparq "..."     # restrict to one apartment
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import TypedDict

from dotenv import load_dotenv
from groq import Groq

from retrieval import TOP_K, RetrievedChunk, retrieve

# --- Configuration ---
load_dotenv()  # pulls GROQ_API_KEY out of .env
GROQ_MODEL = "llama-3.3-70b-versatile"   # fast, strong instruction-following on Groq
TEMPERATURE = 0.1                         # low → faithful to the source text
MIN_SCORE = 0.15                          # drop near-irrelevant chunks before prompting

SYSTEM_PROMPT = """\
You are "The Unofficial Guide," a grounded assistant that answers questions about \
off-campus apartments in downtown San Jose using ONLY tenant reviews retrieved for \
each question.

Follow these rules strictly:

1. GROUNDING. Base every statement solely on the REVIEWS provided in the user message. \
Never use outside knowledge or invent details (fees, dates, names, policies). If the \
reviews do not contain the answer, say so plainly: "The reviews I have don't cover \
that." Do not guess.

2. ATTRIBUTION. The reviews are about specific apartments. Attribute each point to the \
apartment it comes from (e.g., "At Sparq, reviewers say..."). If the question names an \
apartment, only use reviews whose source is that apartment; ignore reviews about other \
buildings even if they sound similar.

3. BOTH SIDES. Reviews for the same building often conflict. When they do, present both \
the positive and the negative rather than collapsing to one verdict (e.g., "Some \
residents say X, while others report the opposite.").

4. STYLE. Be concise and specific. Prefer concrete details that appear in the reviews \
(specific fees, durations, systems) over vague summaries. Do not fabricate quotes."""


class GeneratedAnswer(TypedDict):
    answer: str
    chunks: list[RetrievedChunk]   # the chunks actually sent to the model
    sources: list[str]             # distinct apartments those chunks came from


# Cache the Groq client so we don't recreate it on every call.
_client: Groq | None = None


def _get_client() -> Groq:
    """Create (once) the Groq client, failing clearly if the key is missing."""
    global _client
    if _client is None:
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError(
                "GROQ_API_KEY is not set. Add it to your .env file "
                "(see .env.example): GROQ_API_KEY=your_key_here"
            )
        _client = Groq(api_key=api_key)
    return _client


def _format_context(chunks: list[RetrievedChunk]) -> str:
    """Render retrieved chunks as numbered, source-labelled review blocks.

    Tagging every block with its apartment is what lets the model attribute
    claims correctly and refuse cross-building chunks.
    """
    blocks = []
    for i, c in enumerate(chunks, start=1):
        addr = f" — {c['address']}" if c["address"] else ""
        blocks.append(
            f"[{i}] Apartment: {c['source']}{addr} (relevance {c['score']:.2f})\n"
            f"{c['text']}"
        )
    return "\n\n".join(blocks)


def generate_answer(
    query: str,
    k: int = TOP_K,
    source: str | None = None,
) -> GeneratedAnswer:
    """Retrieve the top-k reviews for `query` and answer from them via Groq.

    `source` optionally restricts retrieval to one apartment (passed straight
    through to `retrieve`). Returns the answer plus the chunks/sources it was
    grounded on, so the UI can surface attribution.
    """
    chunks = retrieve(query, k=k, source=source)

    # Filter out near-irrelevant matches so the model isn't tempted to use them.
    chunks = [c for c in chunks if c["score"] >= MIN_SCORE] or chunks

    if not chunks:
        return GeneratedAnswer(
            answer="The reviews I have don't cover that.",
            chunks=[],
            sources=[],
        )

    user_prompt = (
        f"QUESTION:\n{query}\n\n"
        f"REVIEWS (each block is a separate tenant review; use only these):\n\n"
        f"{_format_context(chunks)}\n\n"
        f"Answer the question using only the reviews above, following the rules."
    )

    completion = _get_client().chat.completions.create(
        model=GROQ_MODEL,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )
    answer = completion.choices[0].message.content.strip()

    # Distinct sources, preserved in retrieval order, for attribution display.
    seen: dict[str, None] = {}
    for c in chunks:
        seen.setdefault(c["source"], None)
    sources = list(seen)

    return GeneratedAnswer(answer=answer, chunks=chunks, sources=sources)


def _print_answer(query: str, result: GeneratedAnswer) -> None:
    print("\n" + "=" * 78)
    print(f"Q: {query}")
    print("=" * 78)
    print(result["answer"])
    print("\n" + "-" * 78)
    print("Sources: " + (", ".join(result["sources"]) or "(none)"))
    for i, c in enumerate(result["chunks"], start=1):
        snippet = c["text"][:120].replace("\n", " ")
        print(f"  [{i}] {c['source']} (score={c['score']:.3f}) {snippet}...")
    print("=" * 78)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Answer a question from reviews via Groq.")
    parser.add_argument("query", nargs="?", help="question to answer")
    parser.add_argument("-k", type=int, default=TOP_K, help="top-k chunks (default 5)")
    parser.add_argument("--source", help="restrict to one apartment")
    args = parser.parse_args()

    query = args.query or (
        "What do reviewers say about package delivery and the package fee at Miro San Jose?"
    )
    try:
        _print_answer(query, generate_answer(query, k=args.k, source=args.source))
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
