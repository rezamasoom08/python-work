import pdfplumber
import pandas as pd

# Define the path to your PDF file
pdf_path = "SVD005924.pdf"

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    # Extract table data from the first page (you can loop through all pages)
    page = pdf.pages[0]
    table = page.extract_table()

    # Convert the table data to a Pandas DataFrame
    df = pd.DataFrame(table)

    # Save the DataFrame to an Excel file
    df.to_excel("extracted_table.xlsx", index=False)

print("Table extracted and saved successfully!")
