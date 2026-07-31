from dataclasses import dataclass
from typing import Any

from app.generation.model import create_chat_model
from app.generation.prompts import AZURE_RAG_PROMPT
from app.retrieval.retriever import create_retriever


@dataclass
class RagResult:
    answer: str
    sources: list[dict[str, Any]]


def format_context(documents) -> str:
    blocks: list[str] = []

    for document in documents:
        metadata = document.metadata

        blocks.append(
            "\n".join(
                [
                    f"Title: {metadata.get('title', metadata.get('file_name'))}",
                    f"Service: {metadata.get('service', 'Azure')}",
                    f"Page: {metadata.get('page_number', 'N/A')}",
                    f"Source: {metadata.get('source_url', metadata.get('source'))}",
                    f"Content: {document.page_content}",
                ]
            )
        )

    return "\n\n---\n\n".join(blocks)


def answer_question(question: str) -> RagResult:
    retriever = create_retriever()
    model = create_chat_model()

    documents = retriever.invoke(question)
    context = format_context(documents)

    prompt = AZURE_RAG_PROMPT.invoke(
        {
            "question": question,
            "context": context,
        }
    )

    response = model.invoke(prompt)

    sources = [
        {
            "title": document.metadata.get(
                "title",
                document.metadata.get("file_name"),
            ),
            "service": document.metadata.get("service"),
            "page": document.metadata.get("page_number"),
            "source_url": document.metadata.get("source_url"),
            "chunk_id": document.metadata.get("chunk_id"),
        }
        for document in documents
    ]

    return RagResult(
        answer=str(response.content),
        sources=sources,
    )