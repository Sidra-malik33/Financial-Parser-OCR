import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import Image
import io

def extract_text_from_image(image_bytes):
    image= Image.open(io.BytesIO(image_bytes))
    text= pytesseract.image_to_string(image)
    return text
