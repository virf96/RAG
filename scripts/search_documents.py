from app.embeddings.factory import create_embeddings
from app.vectorstore.chroma_store import load_chroma_store


def main() -> None:
    embeddings = create_embeddings()
    vector_store = load_chroma_store(embeddings)

    query = input("\nEnter your question: ").strip()

    if not query:
        raise ValueError("The question cannot be empty")

    results = vector_store.similarity_search_with_score(
        query=query,
        k=3,
    )

    print(f"\nQuery: {query}")
    print("\nTop results:")

    for position, (document, distance) in enumerate(results, start=1):
        print("\n" + "=" * 80)
        print(f"Result {position}")
        print(f"Distance: {distance:.4f}")
        print(f"File: {document.metadata.get('file_name')}")
        print(f"Page: {document.metadata.get('page_number')}")
        print(f"Category: {document.metadata.get('category')}")
        print(f"Chunk ID: {document.metadata.get('chunk_id')}")
        print("-" * 80)
        print(document.page_content)


if __name__ == "__main__":
    main()