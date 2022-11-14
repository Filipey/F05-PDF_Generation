import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from models.inspectionPdf import InspectionPdfDTO
from PDF.service import generate_pdf

app = FastAPI()

@app.get("/")
async def hello():
  return {"message": "Server Running"}

@app.post("/pdf")
async def get_inspection_report(pdfDto: InspectionPdfDTO):
  pdf = generate_pdf(pdfDto)

  headers = {'Content-Disposition': f'attachment; filename={pdf}'}
  return FileResponse(pdf, headers=headers, media_type="application/pdf")

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
