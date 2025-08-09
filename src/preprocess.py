import re
import nltk
from nltk.corpus import stopwords  # ✅ fixed import

# Download NLTK stopwords (first time only)
nltk.download('stopwords', quiet=True)  # ✅ fixed typo (nlt → nltk)

def clean_text(text):
    """
    Lowercases, removes special characters, and extra spaces.
    """
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # keep only letters/numbers/spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def remove_stopwords(text):
    """
    Removes common English stopwords.
    """
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return " ".join(filtered_words)

if __name__ == "__main__":
    from ingest import read_file  # ✅ correct import path

    raw_text = read_file("data/sample.txt")
    print("Raw text:", raw_text)

    cleaned = clean_text(raw_text)
    print("\nCleaned text:", cleaned)

    no_stop = remove_stopwords(cleaned)
    print("\nWithout stopwords:", no_stop)
