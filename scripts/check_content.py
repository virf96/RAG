from app.vectorstore.chroma_store import create_vector_store

store = create_vector_store()

terms = [
    "Azure Functions",
    "Container Apps",
    "Azure Container Apps",
    "Blob Storage",
    "Azure Blob Storage",
]

for term in terms:
    print(f"\n========== {term} ==========")

    results = store.get(
        where_document={
            "$contains": term
        }
    )

    print(f"Matches: {len(results['documents'])}")

    for doc in results["documents"][:3]:
        print(doc[:500])
        print("-" * 80)