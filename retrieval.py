"""Milestone 4 — Embedding and retrieval.

Full pipeline (this module covers stages 3 and 4):

    1. Document Ingestion   ingest.load_documents()      [ingest.py]
    2. Chunking             ingest.chunk_text()          [ingest.py]
    3. Embedding + Store    SentenceTransformer +        <-- THIS FILE
                            ChromaDB persistent collection
    4. Retrieval            embed query, similarity      <-- THIS FILE
                            search, top-k = 5
    5. Generation + UI      Groq LLM + Gradio            [milestone 5]

Per planning.md (Retrieval Approach):
  * Embedding model : all-MiniLM-L6-v2 (sentence-transformers), 384-dim
  * Top-k           : 5  (≈ one review per retrieved chunk)
  * Store           : persistent ChromaDB collection holding the vector,
                      the chunk text, and {source, address, ...} metadata.

The same model embeds both the chunks (at index time) and the query (at
search time), so the two live in the same vector space.

Usage:
    python retrieval.py --rebuild        # (re)build the index from documents/
    python retrieval.py "your question"  # query an existing index
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import TypedDict

import chromadb
from sentence_transformers import SentenceTransformer

from ingest import chunk_text, load_documents

# --- Configuration (mirrors the Retrieval Approach section of planning.md) ---
MODEL_NAME = "all-MiniLM-L6-v2"
PERSIST_DIR = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "apartment_reviews"
TOP_K = 5

# Cache the model so we don't reload it on every call within a process.
_model: SentenceTransformer | None = None


class RetrievedChunk(TypedDict):
    text: str
    source: str
    address: str
    source_file: str
    review_index: int
    chunk_index: int
    score: float       # cosine similarity in [0, 1]; higher = more relevant


def get_model() -> SentenceTransformer:
    """Load (once) the shared embedding model used for chunks AND queries."""
    global _model
    if _model is None:
        _model = SentenceTransformer(MODEL_NAME)
    return _model


def _get_collection() -> chromadb.api.models.Collection.Collection:
    """Open the persistent ChromaDB collection (cosine space)."""
    client = chromadb.PersistentClient(path=str(PERSIST_DIR))
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},  # MiniLM is trained for cosine
    )


def _chunk_id(meta: dict) -> str:
    """Deterministic, provenance-carrying id so re-indexing upserts cleanly."""
    return f"{meta['source_file']}::r{meta['review_index']}::c{meta['chunk_index']}"


def build_index(rebuild: bool = False) -> int:
    """Embed every chunk and store it in ChromaDB. Returns the chunk count.

    Loads documents -> chunks them -> embeds each chunk's text with
    all-MiniLM-L6-v2 -> upserts {id, embedding, document, metadata} into the
    persistent collection.

    If `rebuild` is False and the collection is already populated, it skips
    re-embedding (fast no-op). Pass `rebuild=True` to wipe and rebuild.
    """
    client = chromadb.PersistentClient(path=str(PERSIST_DIR))

    if rebuild:
        try:
            client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass  # nothing to delete on a fresh machine

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    chunks = chunk_text(load_documents())

    if not rebuild and collection.count() == len(chunks):
        print(f"Index already built ({collection.count()} chunks). "
              f"Use --rebuild to force.")
        return collection.count()

    texts = [c["text"] for c in chunks]
    ids = [_chunk_id(c["metadata"]) for c in chunks]
    metadatas = [c["metadata"] for c in chunks]

    print(f"Embedding {len(texts)} chunks with {MODEL_NAME} ...")
    model = get_model()
    embeddings = model.encode(
        texts,
        batch_size=64,
        normalize_embeddings=True,   # unit vectors → clean cosine similarity
        show_progress_bar=True,
    ).tolist()

    collection.upsert(
        ids=ids,
        embeddings=embeddings,
        documents=texts,
        metadatas=metadatas,
    )
    print(f"Stored {collection.count()} chunks in ChromaDB at {PERSIST_DIR}")
    return collection.count()


def retrieve(query: str, k: int = TOP_K, source: str | None = None) -> list[RetrievedChunk]:
    """Embed `query` with the same model and return the top-`k` chunks.

    `source` optionally restricts the search to one apartment via a metadata
    filter (e.g. source="Sparq") — useful for building-specific questions to
    avoid cross-building contamination.
    """
    collection = _get_collection()
    if collection.count() == 0:
        raise RuntimeError(
            "The index is empty. Build it first: python retrieval.py --rebuild"
        )

    query_embedding = get_model().encode(
        [query], normalize_embeddings=True
    ).tolist()

    where = {"source": source} if source else None
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k,
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    out: list[RetrievedChunk] = []
    docs = results["documents"][0]
    metas = results["metadatas"][0]
    dists = results["distances"][0]
    for text, meta, dist in zip(docs, metas, dists):
        out.append(
            RetrievedChunk(
                text=text,
                source=meta["source"],
                address=meta["address"],
                source_file=meta["source_file"],
                review_index=meta["review_index"],
                chunk_index=meta["chunk_index"],
                score=round(1.0 - dist, 4),  # cosine distance -> similarity
            )
        )
    return out


def _print_results(query: str, results: list[RetrievedChunk]) -> None:
    print("\n" + "=" * 78)
    print(f"QUERY: {query}")
    print("=" * 78)
    for i, r in enumerate(results, start=1):
        snippet = r["text"][:200].replace("\n", " ")
        print(f"\n[{i}] score={r['score']:.4f}  source={r['source']}")
        print(f"    {snippet}{'...' if len(r['text']) > 200 else ''}")
    print("\n" + "=" * 78)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build index / run a retrieval.")
    parser.add_argument("query", nargs="?", help="question to retrieve chunks for")
    parser.add_argument("--rebuild", action="store_true",
                        help="wipe and rebuild the ChromaDB index from documents/")
    parser.add_argument("-k", type=int, default=TOP_K, help="top-k chunks (default 5)")
    parser.add_argument("--source", help="restrict search to one apartment")
    args = parser.parse_args()

    if args.rebuild:
        build_index(rebuild=True)
    else:
        # Make sure an index exists before querying.
        build_index(rebuild=False)

    # Default demo query = evaluation question #1 from planning.md.
    query = args.query or (
        "What do reviewers say about package delivery and the package fee at Miro San Jose?"
    )
    if args.query is None and not args.rebuild:
        pass  # fall through to demo
    _print_results(query, retrieve(query, k=args.k, source=args.source))
