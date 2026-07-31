from statistics import mean

from app.ingestion.chunking import split_documents
from app.ingestion.cleaning import clean_documents
from app.ingestion.loaders import load_directory


def main() -> None:
    documents = load_directory("data/raw")
    cleaned_documents = clean_documents(documents)
    chunks = split_documents(cleaned_documents)

    chunk_lengths = [
        len(chunk.page_content)
        for chunk in chunks
    ]

    print(f"\nPages loaded: {len(documents)}")
    print(f"Pages after cleaning: {len(cleaned_documents)}")
    print(f"Chunks created: {len(chunks)}")
    print(f"Average chunk length: {mean(chunk_lengths):.2f}")
    print(f"Smallest chunk: {min(chunk_lengths)}")
    print(f"Largest chunk: {max(chunk_lengths)}")

    print("\nFirst chunk metadata:")
    print(chunks[0].metadata)

    print("\nFirst chunk preview:")
    print(chunks[0].page_content[:700])


if __name__ == "__main__":
    main()