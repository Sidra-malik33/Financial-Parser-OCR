from fastapi import FastAPI, UploadFile, File 
from parser import process_pdf
from utils.export_utils import to_json, to_excel
import os 

app= FastAPI()

@app.post("/upload")
async def upload_invoice(file: UploadFile = File(...)):
    contents= await file.read()
    temp_path= f"temp_{file.filename}"
    with open(temp_path, 'wb') as f:
        f.write(contents)
        
    data= process_pdf(temp_path)
    os.remove(temp_path)
    
    json_path= f"output/{file.filename.replace('.pdf', '.json')}" 
    excel_path= f"output/{file.filename.replace('.pdf', '.xlsx')}"
    
    to_json(data, json_path)
    to_excel(data, excel_path)
    
    return {"message": "Parsed successfully", "data": data} 