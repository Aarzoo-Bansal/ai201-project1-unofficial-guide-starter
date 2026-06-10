"""Milestone 5 — Gradio interface.

The user-facing half of stage 5: a simple web UI where a student types a
question about a downtown San Jose apartment and sees a grounded answer plus
the source apartments (and the exact review snippets) it was drawn from.

It wires the full pipeline together: the query is embedded and matched against
the ChromaDB index (retrieval.py), the top reviews are fed to the Groq LLM under
a grounded system prompt (generate.py), and the answer + attribution are shown.

Usage:
    python app.py                 # launches a local web server
    python app.py --share         # also create a public Gradio link
"""

from __future__ import annotations

import argparse

import gradio as gr

from generate import GeneratedAnswer, generate_answer
from retrieval import TOP_K, build_index

# The apartments in the corpus, for the optional source filter dropdown.
# These MUST match the `source` metadata stored in ChromaDB exactly (it comes
# from each file's "# Source:" header), or the metadata filter returns nothing.
APARTMENTS = [
    "Any apartment",
    "Miro San Jose Apartments",
    "One South Market",
    "Avalon at Cahil Park",
    "27 North - Student Housing Apartments",
    "Sparq",
    "The Grad San Jose",
    "The James Apartment",
    "Modera San Pedro Square",
    "The Taft Apartments",
    "The Ryden Apartments",
]

EXAMPLES = [
    "What do reviewers say about package delivery and the package fee at Miro San Jose?",
    "How reliable are the elevators at 27 North, and how does management handle outages?",
    "What problems do residents report with the parking system at Sparq?",
    "How close is The Grad to SJSU campus?",
    "Is Sparq accommodating to pets and emotional support animals (ESAs)?",
]


def _render_sources(result: GeneratedAnswer) -> str:
    """Format the attribution panel: which apartments + which review snippets."""
    if not result["chunks"]:
        return "_No matching reviews._"

    lines = ["**Sources:** " + ", ".join(result["sources"]), "", "**Retrieved reviews:**"]
    for i, c in enumerate(result["chunks"], start=1):
        snippet = c["text"].replace("\n", " ").strip()
        if len(snippet) > 240:
            snippet = snippet[:240] + "…"
        lines.append(f"{i}. *{c['source']}* (relevance {c['score']:.2f}) — {snippet}")
    return "\n".join(lines)


def answer_question(query: str, apartment: str) -> tuple[str, str]:
    """Gradio callback: question + optional apartment → (answer, sources panel)."""
    query = (query or "").strip()
    if not query:
        return "Please enter a question.", ""

    source = None if apartment in (None, "", "Any apartment") else apartment
    try:
        result = generate_answer(query, k=TOP_K, source=source)
    except RuntimeError as e:
        # Most likely a missing GROQ_API_KEY — surface it instead of crashing.
        return f"⚠️ {e}", ""

    return result["answer"], _render_sources(result)


def build_ui() -> gr.Blocks:
    with gr.Blocks(title="The Unofficial Guide — San Jose Apartments") as demo:
        gr.Markdown(
            "# 🏢 The Unofficial Guide\n"
            "Ask about off-campus apartments in downtown San Jose. "
            "Answers are grounded in real tenant reviews — the assistant only uses "
            "what the reviews say and tells you which apartment each point comes from."
        )
        with gr.Row():
            question = gr.Textbox(
                label="Your question",
                placeholder="e.g. What do residents say about parking at Sparq?",
                lines=2,
                scale=4,
            )
            apartment = gr.Dropdown(
                APARTMENTS,
                value="Any apartment",
                label="Limit to apartment (optional)",
                scale=1,
            )
        ask = gr.Button("Ask", variant="primary")

        answer = gr.Markdown(label="Answer")
        sources = gr.Markdown(label="Sources")

        gr.Examples(examples=EXAMPLES, inputs=question)

        ask.click(answer_question, inputs=[question, apartment], outputs=[answer, sources])
        question.submit(answer_question, inputs=[question, apartment], outputs=[answer, sources])

    return demo


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Launch the Unofficial Guide UI.")
    parser.add_argument("--share", action="store_true", help="create a public Gradio link")
    args = parser.parse_args()

    # Make sure the vector index exists before the UI starts taking questions.
    build_index(rebuild=False)

    build_ui().launch(share=args.share)
