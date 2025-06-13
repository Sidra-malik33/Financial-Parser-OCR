import fitz
from utils.ocr_utils import extract_text_from_image
from utils.extract_utils import extract_fields

import os

def process_pdf(file_path):
    doc= fitz.open(file_path)
    full_text= ""
    
    for page_num in range(len(doc)):
        page= doc.load_page(page_num)
        pix= page.get_pixmap(dpi=300)
        image_bytes= pix.tobytes("png")
        text= extract_text_from_image(image_bytes)
        full_text += text + "\n"
        
    fields= extract_fields(full_text)
    return fields

