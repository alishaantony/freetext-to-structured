import os
import json

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None  # Allow running without OpenAI installed

def label_with_ai(data):
    """
    Use OpenAI GPT model to label structured data semantically.
    If API is not set, returns mock labeled data.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key or OpenAI is None:
        # Mock output for demo purposes
        labeled = {}
        for file_path, file_data in data.items():
            if file_data["type"] == "text":
                labeled[file_path] = {
                    "entities_labeled": [
                        {"value": ent[0], "label": ent[1], "semantic_label": "Date" if ent[1] == "DATE" else "Other"}
                        for ent in file_data["entities"]
                    ],
                    "numbers_labeled": [
                        {"value": num, "semantic_label": "Quantity" if int(num) < 100 else "Year"}
                        for num in file_data["numbers"]
                    ]
                }
            else:
                labeled[file_path] = file_data
        return labeled

    # If API key is set, call GPT
    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are a data labeling assistant.
    For the following structured data, add a semantic label for each value:
    {json.dumps(data, indent=2)}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return json.loads(response.output_text)

if __name__ == "__main__":
    # Test with mock data
    test_data = {
        "file.txt": {
            "type": "text",
            "entities": [["August 8 2025", "DATE"]],
            "numbers": ["8", "2025"]
        }
    }
    print(json.dumps(label_with_ai(test_data), indent=4))
