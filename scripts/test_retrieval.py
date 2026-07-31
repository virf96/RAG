from app.retrieval.retriever import create_retriever


def main() -> None:
    retriever = create_retriever()

    questions = [
        "What is Azure Functions?",
        "When should I use Azure Container Apps?",
        "What storage service should I use for unstructured objects?",
        "What are the main Azure architectural components?",
    ]

    for question in questions:
        print(f"\nQUESTION: {question}")

        documents = retriever.invoke(question)

        for rank, document in enumerate(documents, start=1):
            print(f"\nResult {rank}")
            print(document.metadata)
            print(document.page_content[:500])


if __name__ == "__main__":
    main()