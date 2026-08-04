from langchain_google_vertexai import VertexAIEmbeddings

from app.config.settings import get_settings


def create_embedding_model() -> VertexAIEmbeddings:
    """Create the configured Vertex AI embedding model."""

    settings = get_settings()

    return VertexAIEmbeddings(
        model_name=settings.embedding_model,
        project=settings.google_cloud_project,
        location=settings.google_cloud_location,
    )