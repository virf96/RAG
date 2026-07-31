from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdf(file_path: Path) -> list[Document]:
    """Load a PDF and enrich every page with project metadata."""
    if not file_path.exists():
        raise FileNotFoundError(f"PDF not found: {file_path}")

    loader = PyPDFLoader(str(file_path))
    pages = loader.load()

    document_id = file_path.stem
    category = file_path.parent.name

    for page_number, page in enumerate(pages, start=1):
        page.metadata.update(
            {
                "document_id": document_id,
                "file_name": file_path.name,
                "category": category,
                "page_number": page_number,
                "source_type": "pdf",
            }
        )

    return pages


def load_directory(directory: str) -> list[Document]:
    """Load every PDF recursively from a directory."""
    root = Path(directory)

    if not root.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    pdf_files = list(root.rglob("*.pdf"))

    if not pdf_files:
        raise ValueError(f"No PDF files found in: {directory}")

    documents: list[Document] = []

    for file_path in pdf_files:
        documents.extend(load_pdf(file_path))

    return documents