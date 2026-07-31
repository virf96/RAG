from app.ingestion.chunking import split_documents
from app.ingestion.cleaning import clean_documents
from app.ingestion.loaders import load_directory
from app.vectorstore.chroma_store import create_vector_store


def run_ingestion(source_directory: str) -> dict[str, int]:
    documents = load_directory(source_directory)
    cleaned_documents = clean_documents(documents)
    chunks = split_documents(cleaned_documents)

    create_vector_store(chunks)

    return {
        "loaded_pages": len(documents),
        "cleaned_pages": len(cleaned_documents),
        "created_chunks": len(chunks),
    }