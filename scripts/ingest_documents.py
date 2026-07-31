import json

from app.ingestion.pipeline import run_ingestion


if __name__ == "__main__":
    result = run_ingestion("data/raw")
    print(json.dumps(result, indent=2))