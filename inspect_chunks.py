"""Chunk quality inspection — Milestone 3 sanity check.

Prints 5 *representative* chunks (not random: deliberately chosen to span the
range of chunk shapes the splitter produces) and for each asks the key
question from the assignment:

    "Does this chunk make sense on its own? Could someone answer a question
     from this chunk alone, without reading what comes before or after?"

The script can't truly "understand" a chunk, so it surfaces objective signals
that correlate with self-containment:

  * whole_review  - the review produced exactly one chunk (nothing was cut)
  * starts_clean  - begins at a sentence/capital, not mid-thought
  * ends_clean    - ends on terminal punctuation, not mid-sentence

A chunk that is a whole review, or that both starts and ends cleanly, is very
likely answerable on its own. A mid-review fragment that starts lowercase or
ends mid-sentence probably needs its neighbors.

Run:  python inspect_chunks.py
"""

from __future__ import annotations

from collections import defaultdict

from ingest import Chunk, chunk_text, load_documents

# Characters that signal a chunk *begins* as a continuation of a prior chunk.
_CONTINUATION_START = set(".,;:)]}-—…’\"”")
# Characters that signal a chunk *ends* on a complete thought.
_TERMINAL_END = (".", "!", "?", '"', "”", ")", ":")


def starts_clean(text: str) -> bool:
    """True if the chunk opens like the start of a sentence, not mid-thought."""
    first = text.lstrip()[:1]
    if not first:
        return False
    if first in _CONTINUATION_START:
        return False
    # Lowercase opening usually means we cut into the middle of a sentence.
    return not first.islower()


def ends_clean(text: str) -> bool:
    """True if the chunk closes on terminal punctuation."""
    return text.rstrip().endswith(_TERMINAL_END)


def verdict(is_whole: bool, clean_start: bool, clean_end: bool) -> str:
    if is_whole:
        return "SELF-CONTAINED (whole review — nothing was cut)"
    if clean_start and clean_end:
        return "LIKELY self-contained (clean sentence boundaries)"
    if clean_start and not clean_end:
        return "PARTIAL (starts clean but trails off mid-sentence)"
    if not clean_start and clean_end:
        return "PARTIAL (opens mid-thought — needs the previous chunk)"
    return "NOT self-contained (cut on both ends)"


def representative_chunks(chunks: list[Chunk]) -> list[tuple[str, Chunk, bool]]:
    """Pick 5 chunks that represent the variety the splitter produces.

    Returns (label, chunk, is_whole_review) tuples.
    """
    # Group chunks back into their source review to know which were split.
    groups: dict[tuple[str, int], list[Chunk]] = defaultdict(list)
    for c in chunks:
        key = (c["metadata"]["source_file"], c["metadata"]["review_index"])
        groups[key].append(c)

    whole_reviews = [g[0] for g in groups.values() if len(g) == 1]
    split_reviews = sorted(
        (g for g in groups.values() if len(g) > 1),
        key=lambda g: len(g),
        reverse=True,
    )

    whole_reviews.sort(key=lambda c: len(c["text"]))
    selected: list[tuple[str, Chunk, bool]] = []

    # 1. Shortest whole review — the easy, clearly self-contained case.
    if whole_reviews:
        selected.append(("Short whole review", whole_reviews[0], True))

    # 2. A mid-length whole review from a different source for variety.
    if len(whole_reviews) > 1:
        mid = whole_reviews[len(whole_reviews) // 2]
        selected.append(("Medium whole review", mid, True))

    # 3 & 4. First and a middle chunk of the longest split review.
    if split_reviews:
        longest = split_reviews[0]
        selected.append(("First chunk of a long split review", longest[0], False))
        middle = longest[len(longest) // 2]
        selected.append(("Middle chunk of a long split review", middle, False))

    # 5. Last chunk of the *second* longest split review (different review).
    if len(split_reviews) > 1:
        second = split_reviews[1]
        selected.append(("Last chunk of another split review", second[-1], False))

    return selected[:5]


def inspect_chunks(chunks: list[Chunk]) -> None:
    samples = representative_chunks(chunks)
    print("=" * 78)
    print("CHUNK SELF-CONTAINMENT INSPECTION  (5 representative chunks)")
    print("=" * 78)

    for i, (label, chunk, is_whole) in enumerate(samples, start=1):
        text = chunk["text"]
        meta = chunk["metadata"]
        clean_start = starts_clean(text)
        clean_end = ends_clean(text)

        print(f"\n[{i}] {label}")
        print("    metadata (as stored on the chunk):")
        for key, value in meta.items():
            print(f"      {key}: {value}")
        print("    analysis (derived here, not stored):")
        print(f"      length      : {len(text)} chars")
        print(f"      whole_review: {is_whole}")
        print(f"      starts_clean: {clean_start}    ends_clean: {clean_end}")
        print(f"      >> {verdict(is_whole, clean_start, clean_end)}")
        print("    ---- text ----")
        for line in text.splitlines() or [text]:
            print(f"    | {line}")

    print("\n" + "=" * 78)


if __name__ == "__main__":
    docs = load_documents()
    all_chunks = chunk_text(docs)
    inspect_chunks(all_chunks)
