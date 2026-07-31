from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.config.settings import get_settings


def create_embeddings() -> GoogleGenerativeAIEmbeddings:
    settings = get_settings()

    return GoogleGenerativeAIEmbeddings(
        model=settings.embedding_model,
        project=settings.google_cloud_project,
        location=settings.google_cloud_location,
    )