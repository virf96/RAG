from collections import Counter

from app.ingestion.loaders import load_directory


def main() -> None:
    documents = load_directory("data/raw")

    print(f"\nTotal pages loaded: {len(documents)}")

    pages_by_file = Counter(
        document.metadata["file_name"]
        for document in documents
    )

    print("\nDocuments found:")

    for file_name, page_count in pages_by_file.items():
        print(f"- {file_name}: {page_count} pages")

    print("\nFirst page preview:")

    first_document = documents[0]

    print(first_document.metadata)
    print(first_document.page_content[:500])


if __name__ == "__main__":
    main()