import hashlib

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_content_hash(text: str) -> str:
    """Create a deterministic hash from normalized text."""
    normalized_text = " ".join(text.lower().split())

    return hashlib.sha256(
        normalized_text.encode("utf-8")
    ).hexdigest()


def split_documents(
    documents: list[Document],
    chunk_size: int = 1000,
    chunk_overlap: int = 150,
) -> list[Document]:
    """Split documents while preserving and validating metadata."""
    if not documents:
        raise ValueError("The documents list cannot be empty")

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero")

    if chunk_overlap < 0:
        raise ValueError("chunk_overlap cannot be negative")

    if chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be smaller than chunk_size"
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n## ",
            "\n### ",
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
    )

    chunks = splitter.split_documents(documents)

    for index, chunk in enumerate(chunks):
        content_hash = create_content_hash(chunk.page_content)

        document_id = chunk.metadata.get(
            "document_id",
            chunk.metadata.get("file_name", "unknown-document"),
        )

        original_page = chunk.metadata.get("page", 0)

        page_number = chunk.metadata.get(
            "page_number",
            original_page + 1,
        )

        chunk.metadata.update(
            {
                "document_id": document_id,
                "page_number": page_number,
                "chunk_id": f"{document_id}-{page_number}-{index:05d}",
                "content_hash": content_hash,
                "chunk_length": len(chunk.page_content),
            }
        )

    return chunks