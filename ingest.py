"""Milestone 3 — Document ingestion and chunking.

Implements the Chunking Strategy from planning.md:

  1. Load every .txt file in documents/, parsing the
     "# Source:" / "# Address:" header.
  2. Split each document on blank lines to isolate individual reviews
     (the natural unit of meaning in this corpus).
  3. Run a RecursiveCharacterTextSplitter (chunk_size=500, overlap=75)
     within each review so short reviews stay whole and long multi-topic
     reviews are subdivided at natural boundaries.

Every chunk carries {source, address} metadata so the retrieval stage can
attribute each chunk to the correct apartment.

Run directly to load, chunk, and print verification stats:

    python ingest.py
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import TypedDict

from langchain_text_splitters import RecursiveCharacterTextSplitter

# --- Configuration (mirrors the Chunking Strategy section of planning.md) ---
DOCUMENTS_DIR = Path(__file__).parent / "documents"
CHUNK_SIZE = 500       # characters
CHUNK_OVERLAP = 75     # characters (15% of chunk size)

# Matches one or more blank lines (lines with only whitespace) between reviews.
_BLANK_LINE_SPLIT = re.compile(r"\n\s*\n+")


class Document(TypedDict):
    source: str            # apartment name from "# Source:"
    address: str           # address from "# Address:" ("" if not provided)
    source_file: str       # filename, for traceability
    reviews: list[str]     # individual reviews, one per blank-line block


class Chunk(TypedDict):
    text: str
    metadata: dict[str, str | int]


def _clean(text: str) -> str:
    """Light normalization: unify line endings and trim whitespace.

    Internal single newlines are preserved (some reviews span several lines),
    but leading/trailing whitespace is removed.
    """
    return text.replace("\r\n", "\n").replace("\r", "\n").strip()


def load_documents(documents_dir: Path = DOCUMENTS_DIR) -> list[Document]:
    """Read every .txt file in `documents_dir`, parse its header, and split the
    body into individual reviews on blank lines.

    Each file looks like::

        # Source: One South Market
        # Address: 1 S Market St, San Jose, CA 95113

        <review 1>

        <review 2>
        ...
    """
    documents: list[Document] = []

    for path in sorted(documents_dir.glob("*.txt")):
        raw = _clean(path.read_text(encoding="utf-8"))

        source = ""
        address = ""
        body_lines: list[str] = []
        for line in raw.split("\n"):
            stripped = line.strip()
            if stripped.startswith("# Source:"):
                source = stripped[len("# Source:"):].strip()
            elif stripped.startswith("# Address:"):
                address = stripped[len("# Address:"):].strip()
            elif stripped.startswith("#"):
                # Any other comment/header line — skip it, don't treat as text.
                continue
            else:
                body_lines.append(line)

        # Fall back to the filename if a "# Source:" header is missing.
        if not source:
            source = path.stem.replace("_", " ").title()

        body = "\n".join(body_lines)
        reviews = [r.strip() for r in _BLANK_LINE_SPLIT.split(body) if r.strip()]

        documents.append(
            Document(
                source=source,
                address=address,
                source_file=path.name,
                reviews=reviews,
            )
        )

    return documents


def chunk_text(
    documents: list[Document],
    chunk_size: int = CHUNK_SIZE,
    chunk_overlap: int = CHUNK_OVERLAP,
) -> list[Chunk]:
    """Turn loaded documents into chunks tagged with {source, address} metadata.

    Reviews are already isolated by `load_documents`. Each review is passed
    through a RecursiveCharacterTextSplitter: reviews under `chunk_size` stay
    whole, while longer ones are split at natural boundaries (paragraph, line,
    space) with `chunk_overlap` characters carried across each split.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )

    chunks: list[Chunk] = []
    for doc in documents:
        for review_index, review in enumerate(doc["reviews"]):
            pieces = splitter.split_text(review)
            for piece in pieces:
                piece = piece.strip()
                if not piece:
                    continue
                chunks.append(
                    Chunk(
                        text=piece,
                        metadata={
                            "source": doc["source"],
                            "address": doc["address"],
                            "source_file": doc["source_file"],
                            "review_index": review_index,
                            "chunk_index": len(chunks),
                        },
                    )
                )

    return chunks


def _print_verification(documents: list[Document], chunks: list[Chunk]) -> None:
    """Print the stats planning.md calls for: chunk count + spot checks."""
    total_reviews = sum(len(d["reviews"]) for d in documents)
    print("=" * 70)
    print("INGESTION + CHUNKING SUMMARY")
    print("=" * 70)
    print(f"Documents loaded : {len(documents)}")
    print(f"Reviews isolated : {total_reviews}")
    print(f"Total chunks     : {len(chunks)}")
    print(f"Chunk size / overlap : {CHUNK_SIZE} / {CHUNK_OVERLAP} chars")

    print("\nChunks per source:")
    per_source: dict[str, int] = {}
    for c in chunks:
        per_source[c["metadata"]["source"]] = per_source.get(c["metadata"]["source"], 0) + 1
    for source, count in sorted(per_source.items()):
        print(f"  {count:>3}  {source}")

    # Confirm every chunk carries source metadata.
    missing = [c for c in chunks if not c["metadata"].get("source")]
    print(f"\nChunks missing a source tag: {len(missing)}")

    # Spot-check: a short review should remain a single chunk.
    short = min(
        (r for d in documents for r in d["reviews"]),
        key=len,
        default="",
    )
    print("\n--- Spot check: shortest review (should be 1 whole chunk) ---")
    print(f"length = {len(short)} chars")
    print(repr(short[:300]))

    # Spot-check: a long review should be split into several chunks.
    longest_review = max(
        ((d, r) for d in documents for r in d["reviews"]),
        key=lambda dr: len(dr[1]),
        default=None,
    )
    if longest_review is not None:
        doc, review = longest_review
        pieces = chunk_text([Document(
            source=doc["source"], address=doc["address"],
            source_file=doc["source_file"], reviews=[review],
        )])
        print("\n--- Spot check: longest review (should split into >1 chunk) ---")
        print(f"source = {doc['source']!r}")
        print(f"review length = {len(review)} chars -> {len(pieces)} chunks")
        for i, p in enumerate(pieces):
            print(f"  chunk {i} ({len(p['text'])} chars): {p['text'][:90]!r}...")
    print("=" * 70)


if __name__ == "__main__":
    docs = load_documents()
    all_chunks = chunk_text(docs)
    _print_verification(docs, all_chunks)
