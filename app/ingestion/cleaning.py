import re

from langchain_core.documents import Document


def normalize_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def clean_documents(documents: list[Document]) -> list[Document]:
    cleaned: list[Document] = []

    for document in documents:
        content = normalize_text(document.page_content)

        if len(content) < 100:
            continue

        cleaned.append(
            Document(
                page_content=content,
                metadata=document.metadata.copy(),
            )
        )

    return cleaned