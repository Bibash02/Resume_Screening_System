import os

def extract_text_from_txt(file_path):
    with open(file_path, "r", encoding="utf-8", errors = "ignore") as f:
        return f.read()

def extract_resume_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        return extract_text_from_txt(file_path)
    
    raise ValueError("Unsupported file format. Use .txt for now.")
