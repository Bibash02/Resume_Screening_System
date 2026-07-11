import os
import pdfplumber
from docx import Document

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8", errors = "ignore") as f:
        return f.read()
    
def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text

            if page_text:
                text += page_text + "\n"

def extract_text_from_docx(file_path):
    document = Document(file_path)

    text = []

    for paragraph in document.paragraphs:
        text.append(paragraph.text)
    return "\n".join(text)


def extract_resume_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return extract_text_from_txt(file_path)
    elif ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format.")
    
    raise ValueError("Unsupported file format. Use .txt for now.")
