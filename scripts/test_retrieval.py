from app.retrieval.service import retrieve_documents


def main() -> None:
    questions = [
        "What is Azure Functions?",
        "When should I use Azure Container Apps?",
        "What storage service should I use for unstructured objects?",
        "What are the main Azure architectural components?",
    ]

    for question in questions:
        result = retrieve_documents(question)

        print(f"\nQUESTION: {question}")
        print(f"Retrieval latency: {result.duration_seconds:.4f}s")
        print(f"Documents retrieved: {result.retrieved_count}")

        for rank, document in enumerate(result.documents, start=1):
            print(f"\nResult {rank}")
            print(f"File: {document.metadata.get('file_name')}")
            print(f"Page: {document.metadata.get('page_number')}")
            print(f"Chunk: {document.metadata.get('chunk_id')}")
            print(document.page_content[:500])


if __name__ == "__main__":
    main()