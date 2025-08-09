import json
from src.extractor import process_file
from src.ai_labeler import label_with_ai

def main():
    file_paths = [
        "data/sample.txt",
        "data/sample.pdf",
        "data/sample.xlsx"
    ]

    # Step 1 — Extract structured data
    results = {}
    for path in file_paths:
        results[path] = process_file(path)

    # Step 2 — AI semantic labeling
    labeled_results = label_with_ai(results)

    print(json.dumps(labeled_results, indent=4))

if __name__ == "__main__":
    main()
