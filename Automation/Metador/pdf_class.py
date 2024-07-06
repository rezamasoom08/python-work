import PyPDF2
from fpdf import FPDF

pdf = FPDF()

class MASOOM(FPDF):
    def header(self):
        self.image("rhce.jpg", 170, 10, 20)
        self.set_font("Arial", "B", 15)
        self.cell(80)
        self.cell(30, 10, "Invoice", 1, 0, "C")
        self.ln(20)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + "/{nb}", 0, 0, "C")
    
pdf = MASOOM()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font("Times", '', 12)
for i in range(1, 30):
    pdf.cell(0, 10, 'Invoice Line Number: ' + str(i), 0, 1)

pdf.output("sample.pdf", "F")