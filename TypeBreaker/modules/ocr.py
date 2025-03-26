import pytesseract
from PIL import Image


def ocr (image) :

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image).lower()

    return text