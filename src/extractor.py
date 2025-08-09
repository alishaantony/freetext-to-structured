import spacy
import re
from src.preprocess import clean_text, remove_stopwords
from src.ingest import read_file
import pandas as pd

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    """
    Extract named entities from text using spaCy.
    """
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def extract_numbers(text):
    """
    Extract numbers from text using regex.
    """
    return re.findall(r'\b\d+(?:\.\d+)?\b', text)

def process_file(file_path):
    """
    Process any supported file type and return structured data.
    """
    content = read_file(file_path)

    # Excel is already structured
    if isinstance(content, pd.DataFrame):
        return {
            "type": "excel",
            "data": content.to_dict(orient="records")
        }

    # For text/PDF
    cleaned = clean_text(content)
    no_stop = remove_stopwords(cleaned)
    entities = extract_entities(no_stop)
    numbers = extract_numbers(no_stop)

    return {
        "type": "text",
        "entities": entities,
        "numbers": numbers
    }

if __name__ == "__main__":
    txt_result = process_file("data/sample.txt")
    pdf_result = process_file("data/sample.pdf")
    excel_result = process_file("data/sample.xlsx")

    print("\nTXT Result:", txt_result)
    print("\nPDF Result:", pdf_result)
    print("\nExcel Result:", excel_result)
