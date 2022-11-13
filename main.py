import uvicorn
from fastapi import FastAPI

from models.inspectionPdf import InspectionPdfDTO
from PDF.service import generate_pdf

app = FastAPI()

@app.get("/")
async def hello():
  return {"message": "Server Running"}

@app.post("/pdf")
async def get_inspection_report(pdfDto: InspectionPdfDTO):
  generate_pdf(pdfDto)
  return pdfDto

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
