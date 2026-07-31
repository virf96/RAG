from app.embeddings.factory import create_embeddings
from app.ingestion.chunking import split_documents
from app.ingestion.cleaning import clean_documents
from app.ingestion.loaders import load_directory


def main() -> None:
    documents = load_directory("data/raw")
    cleaned_documents = clean_documents(documents)
    chunks = split_documents(cleaned_documents)

    embeddings = create_embeddings()

    sample_text = chunks[0].page_content
    vector = embeddings.embed_query(sample_text)

    print(f"\nSample text length: {len(sample_text)}")
    print(f"Embedding dimensions: {len(vector)}")
    print(f"First 10 values: {vector[:10]}")

    if not vector:
        raise ValueError("The embedding vector is empty")

    if not all(isinstance(value, float) for value in vector):
        raise TypeError("The embedding contains non-float values")

    print("\nEmbedding test completed successfully.")


if __name__ == "__main__":
    main()