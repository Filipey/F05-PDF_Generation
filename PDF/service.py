from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

from models.inspectionPdf import InspectionPdfDTO

MPMG_logo = ImageReader('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAh1FmzGdI-yOVfQFas-ZPtLdNMRjky0lVlhxPed8C&s')

PDF_SIDE_SPACING = 24.45
PDF_TOP_SPACING = 8.10

PDF_SIDE_INITIAL_VALUE = 20
PDF_TOP_INITIAL_VALUE = 100


def __mm_to_p(mm):
  return mm / 0.352777


def generate_pdf(data: InspectionPdfDTO):
  pdf = canvas.Canvas(f"relatorio-vistoria-{getattr(data, 'inspection_id')}.pdf", pagesize=A4)
  
  pdf.drawImage(MPMG_logo,__mm_to_p(PDF_SIDE_INITIAL_VALUE), __mm_to_p(250) , width=150, height=70)
  pdf.drawString(__mm_to_p(110), __mm_to_p(266) , '   Procuradoria-Geral de Justiça')
  pdf.drawString(__mm_to_p(110), __mm_to_p(260), 'Centro de Apoio Técnico - CEAT')
  pdf.drawString(__mm_to_p(110), __mm_to_p(255), '        Setor de Engenharia')

  pdf.setFont("Helvetica-Bold", 14)
  pdf.drawString(__mm_to_p(70), __mm_to_p(235), "Relatório de Vistoria")
  pdf.setFont("Helvetica", 12)

  pdf.drawString(__mm_to_p(30), __mm_to_p(220), f"Local: {getattr(data, 'local')}")
  pdf.drawString(__mm_to_p(30), __mm_to_p(210), f"Data da Vistoria: {getattr(data, 'inspection_date')}")
  pdf.save()

