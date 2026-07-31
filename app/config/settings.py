from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_cloud_project: str
    google_cloud_location: str = "us-central1"
    google_genai_use_vertexai: bool = True

    chat_model: str = "gemini-2.5-flash"
    embedding_model: str = "gemini-embedding-001"

    vector_store: str = "chroma"
    chroma_directory: str = "./chroma_db"
    chroma_collection: str = "azure-documents"

    chunk_size: int = 1000
    chunk_overlap: int = 150
    retrieval_k: int = 5

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()