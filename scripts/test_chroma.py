from app.embeddings.factory import create_embeddings
from app.ingestion.chunking import split_documents
from app.ingestion.cleaning import clean_documents
from app.ingestion.loaders import load_directory
from app.vectorstore.chroma_store import create_chroma_store


def main() -> None:
    documents = load_directory("data/raw")
    cleaned_documents = clean_documents(documents)
    chunks = split_documents(cleaned_documents)

    embeddings = create_embeddings()

    vector_store = create_chroma_store(
        documents=chunks,
        embeddings=embeddings,
    )

    print(f"\nChunks indexed: {len(chunks)}")

    query = (
        "What factors should be considered when designing "
        "a cloud application?"
    )

    results = vector_store.similarity_search_with_score(
        query=query,
        k=3,
    )

    print(f"\nQuery: {query}")
    print("\nTop results:")

    for position, (document, score) in enumerate(results, start=1):
        print(f"\nResult {position}")
        print(f"Score: {score}")
        print(f"File: {document.metadata.get('file_name')}")
        print(f"Page: {document.metadata.get('page_number')}")
        print(f"Category: {document.metadata.get('category')}")
        print(f"Chunk ID: {document.metadata.get('chunk_id')}")
        print("\nContent:")
        print(document.page_content[:600])


if __name__ == "__main__":
    main()