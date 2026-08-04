from app.config.settings import get_settings
from app.embeddings.factory import create_embeddings
from app.ingestion.chunking import split_documents
from app.ingestion.cleaning import clean_documents
from app.ingestion.loaders import load_directory
from app.vectorstore.chroma_store import create_chroma_store


def main() -> None:
    settings = get_settings()

    documents = load_directory("data/raw")
    cleaned_documents = clean_documents(documents)
    chunks = split_documents(cleaned_documents)

    embeddings = create_embeddings()

    vector_store = create_chroma_store(
        documents=chunks,
        embeddings=embeddings,
        persist_directory=settings.chroma_directory,
        collection_name=settings.chroma_collection,
    )

    indexed_count = vector_store._collection.count()

    print("\nIndexing completed successfully.")
    print(f"Pages loaded: {len(documents)}")
    print(f"Pages cleaned: {len(cleaned_documents)}")
    print(f"Chunks generated: {len(chunks)}")
    print(f"Records stored in Chroma: {indexed_count}")


if __name__ == "__main__":
    main()