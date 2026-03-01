from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

def generate_pdf(report_text, filename="research_report.pdf"):
    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    paragraphs = report_text.split("\n")

    for para in paragraphs:
        elements.append(Paragraph(para, style))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)
