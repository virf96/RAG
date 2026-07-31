from langchain_google_genai import ChatGoogleGenerativeAI

from app.config.settings import get_settings


def create_chat_model() -> ChatGoogleGenerativeAI:
    settings = get_settings()

    return ChatGoogleGenerativeAI(
        model=settings.chat_model,
        project=settings.google_cloud_project,
        location=settings.google_cloud_location,
        vertexai=True,
        temperature=0,
    )