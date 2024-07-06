from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os

def extract_metadata_to_pdf(file_path, output_pdf):
    # Get metadata of the file
    metadata = {}
    metadata['Filename'] = os.path.basename(file_path)
    metadata['Filepath'] = file_path
    metadata['Size'] = os.path.getsize(file_path)

    # Create a PDF document
    doc = SimpleDocTemplate(output_pdf, pagesize=letter)
    elements = []

    # Add metadata to the PDF
    data = [[key, value] for key, value in metadata.items()]
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    # Build the PDF document
    doc.build(elements)

if __name__ == "__main__":
    # Path to the file you want to extract metadata from
    file_path = "C:/Users/Mreza/Documents/Study/Cyber Security/CyberSecurity.pdf"

    # Output PDF file where metadata will be stored
    output_pdf = "metadata.pdf"

    extract_metadata_to_pdf(file_path, output_pdf)
