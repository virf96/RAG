from dataclasses import dataclass
from time import perf_counter
from typing import Any

from app.retrieval.retriever import create_retriever


@dataclass(frozen=True)
class RetrievalResult:
    documents: list[Any]
    duration_seconds: float
    retrieved_count: int


def retrieve_documents(question: str) -> RetrievalResult:
    """Retrieve relevant documents for a user question."""

    normalized_question = question.strip()

    if not normalized_question:
        raise ValueError("Question cannot be empty")

    retriever = create_retriever()

    started_at = perf_counter()
    documents = retriever.invoke(normalized_question)
    duration_seconds = perf_counter() - started_at

    return RetrievalResult(
        documents=documents,
        duration_seconds=duration_seconds,
        retrieved_count=len(documents),
    )