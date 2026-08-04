from app.vectorstore.chroma_store import create_vector_store


def main() -> None:
    vector_store = create_vector_store()

    questions = [
        "What is Azure Functions?",
        "When should I use Azure Container Apps?",
        "What storage service should I use for unstructured objects?",
        "What are the main Azure architectural components?",
    ]

    for question in questions:
        print(f"\n{'=' * 100}")
        print(f"QUESTION: {question}")

        results = vector_store.similarity_search_with_score(
            query=question,
            k=5,
        )

        for rank, (document, distance) in enumerate(results, start=1):
            print(f"\nResult {rank}")
            print(f"Distance: {distance:.4f}")
            print(f"File: {document.metadata.get('file_name')}")
            print(f"Page: {document.metadata.get('page_number')}")
            print(f"Chunk ID: {document.metadata.get('chunk_id')}")
            print(document.page_content[:500])


if __name__ == "__main__":
    main()