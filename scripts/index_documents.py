from app.indexing.service import index_directory


def main() -> None:
    result = index_directory("data/raw")

    print("\nIndexing completed successfully.")
    print(f"Pages loaded: {result.pages_loaded}")
    print(f"Pages cleaned: {result.pages_cleaned}")
    print(f"Chunks generated: {result.chunks_generated}")
    print(f"Records stored: {result.records_stored}")
    print(f"Duration: {result.duration_seconds:.2f} seconds")


if __name__ == "__main__":
    main()