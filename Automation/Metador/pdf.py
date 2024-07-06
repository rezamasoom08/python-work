import PyPDF2
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('helvetica', size = 12)
pdf.cell(200, 20, txt = "Hello EDMS Team", ln = 1, align = "C")
pdf.cell(txt = "We are Teva EDMS team and support all legacy systems.")
pdf.output("edms.pdf")
