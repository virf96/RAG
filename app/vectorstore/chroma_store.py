from pathlib import Path
from app.embeddings.factory import create_embeddings

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

from app.config.settings import get_settings

settings = get_settings()
embeddings = create_embeddings()

def create_chroma_store(
    documents=list[Document],
    embeddings=embeddings,
    persist_directory=settings.chroma_directory,
    collection_name=settings.chroma_collection,
) -> Chroma:
    """Create and persist a Chroma vector store."""

    if not documents:
        raise ValueError("The documents list cannot be empty")

    persist_path = Path(persist_directory)
    persist_path.mkdir(parents=True, exist_ok=True)

    ids = [
        document.metadata["chunk_id"]
        for document in documents
    ]

    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        ids=ids,
        collection_name=collection_name,
        persist_directory=str(persist_path),
    )

    return vector_store


def load_chroma_store(
    embeddings: Embeddings,
    persist_directory: str,
    collection_name: str,
) -> Chroma:
    """Load an existing Chroma vector store."""

    persist_path = Path(persist_directory)

    if not persist_path.exists():
        raise FileNotFoundError(
            f"Chroma directory not found: {persist_path.resolve()}"
        )

    return Chroma(
        embedding_function=embeddings,
        collection_name=collection_name,
        persist_directory=str(persist_path),
    )


def create_vector_store() -> Chroma:
    """Load the configured persisted Chroma vector store."""

    settings = get_settings()
    embeddings = create_embeddings()

    return load_chroma_store(
        embeddings=embeddings,
        persist_directory=settings.chroma_directory,
        collection_name=settings.chroma_collection,
    )