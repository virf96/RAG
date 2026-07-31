from app.ingestion.cleaning import clean_documents
from app.ingestion.loaders import load_directory


def main() -> None:
    documents = load_directory("data/raw")
    cleaned_documents = clean_documents(documents)

    print(f"\nPages loaded: {len(documents)}")
    print(f"Pages after cleaning: {len(cleaned_documents)}")
    print(f"Pages removed: {len(documents) - len(cleaned_documents)}")

    first_document = cleaned_documents[0]

    print("\nCleaned page preview:")
    print(first_document.metadata)
    print(first_document.page_content[:500])


if __name__ == "__main__":
    main()