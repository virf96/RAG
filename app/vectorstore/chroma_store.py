from langchain_chroma import Chroma
from langchain_core.documents import Document

from app.config.settings import get_settings
from app.embeddings.factory import create_embeddings


def create_vector_store(
    documents: list[Document] | None = None,
) -> Chroma:
    settings = get_settings()
    embeddings = create_embeddings()

    vector_store = Chroma(
        collection_name=settings.chroma_collection,
        embedding_function=embeddings,
        persist_directory=settings.chroma_directory,
    )

    if documents:
        ids = [doc.metadata["chunk_id"] for doc in documents]
        vector_store.add_documents(documents=documents, ids=ids)

    return vector_store