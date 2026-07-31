from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(file_path: Path) -> list[Document]:
    loader = PyPDFLoader(str(file_path))
    pages = loader.load()

    category = file_path.parent.name

    for page_number, page in enumerate(pages, start=1):
        page.metadata.update(
            {
                "file_name": file_path.name,
                "category": category,
                "page_number": page_number,
                "source_type": "pdf",
            }
        )

    return pages


def load_directory(directory: str) -> list[Document]:
    root = Path(directory)

    if not root.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    documents: list[Document] = []

    for file_path in root.rglob("*.pdf"):
        documents.extend(load_pdf(file_path))

    if not documents:
        raise ValueError(f"No PDF documents found in {directory}")

    return documents