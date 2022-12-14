from typing import List

from pydantic import BaseModel

from models.pdfPhoto import PdfPhoto


class Inspector(BaseModel):
  name: str
  role: str


class InspectionPdfDTO(BaseModel):
  inspection_id: str
  local: str
  inspection_date: str
  content: List[PdfPhoto]
  inspector: Inspector