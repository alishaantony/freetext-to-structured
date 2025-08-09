import os
import pdfplumber
import pandas as pd

def read_file(file_path):
    """
    Reads a file and returns its text content as a string.
    Supports .txt, .pdf, and .xlsx files.
    """
    # Get the file extension (lowercase)
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return text

    elif ext == '.pdf':
        text = ''
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + '\n'
        return text

    elif ext in ['.xls', '.xlsx']:
        # Read all sheets and combine text
        df_dict = pd.read_excel(file_path, sheet_name=None)
        text = ''
        for sheet_name, df in df_dict.items():
            text += f"Sheet: {sheet_name}\n"
            text += df.to_string(index=False) + '\n\n'
        return text

    else:
        raise ValueError(f"Unsupported file type: {ext}")

# Simple test when running this file directly
if __name__ == "__main__":
    sample_txt = 'data/sample.txt'
    sample_pdf = 'data/sample.pdf'
    sample_xlsx = 'data/sample.xlsx'

    print("Reading TXT file:")
    print(read_file(sample_txt))

    print("\nReading PDF file:")
    print(read_file(sample_pdf))

    print("\nReading Excel file:")
    print(read_file(sample_xlsx))
