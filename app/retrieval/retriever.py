from app.config.settings import get_settings
from app.vectorstore.chroma_store import create_vector_store


def create_retriever():
    settings = get_settings()
    vector_store = create_vector_store()

    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": settings.retrieval_k},
    )