from dataclasses import dataclass
from time import perf_counter

from app.config.settings import get_settings
from app.embeddings.factory import create_embeddings
from app.ingestion.chunking import split_documents
from app.ingestion.cleaning import clean_documents
from app.ingestion.loaders import load_directory
from app.vectorstore.chroma_store import create_chroma_store


@dataclass(frozen=True)
class IndexingResult:
    pages_loaded: int
    pages_cleaned: int
    chunks_generated: int
    records_stored: int
    duration_seconds: float


def index_directory(directory: str) -> IndexingResult:
    """Execute the document indexing pipeline."""

    started_at = perf_counter()
    settings = get_settings()

    documents = load_directory(directory)
    cleaned_documents = clean_documents(documents)
    chunks = split_documents(cleaned_documents)
    embeddings = create_embeddings()

    vector_store = create_chroma_store(
        documents=chunks,
        embeddings=embeddings,
        persist_directory=settings.chroma_directory,
        collection_name=settings.chroma_collection,
    )

    duration_seconds = perf_counter() - started_at

    return IndexingResult(
        pages_loaded=len(documents),
        pages_cleaned=len(cleaned_documents),
        chunks_generated=len(chunks),
        records_stored=vector_store._collection.count(),
        duration_seconds=duration_seconds,
    )