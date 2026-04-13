import fitz
import docx
import pytesseract
from PIL import Image


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_pdf(file_path)
    elif file_path.endswith(".docx"):
        return extract_docx(file_path)
    elif file_path.endswith((".png", ".jpg", ".jpeg")):
        return extract_image(file_path)
    elif file_path.endswith(".txt"):
        with open(file_path) as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format")


def extract_pdf(path):
    text = ""
    doc = fitz.open(path)
    for page in doc:
        text += page.get_text()
    return text


def extract_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_image(path):
    return pytesseract.image_to_string(Image.open(path))