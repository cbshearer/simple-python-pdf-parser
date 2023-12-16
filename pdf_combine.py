# pdf_combine.py
from PyPDF2 import PdfReader, PdfWriter
import os

source_dir = "c:\\users\\chris\\pdfs"
target_dir = "c:\\temp"
target_file = "out.pdf"
merged_pdf = PdfWriter()

for filename in os.listdir(source_dir):
    if filename.endswith(".pdf"):
        print(f"Combining: {filename}")
        absolute_path = os.path.join(source_dir, filename)
        with open(absolute_path, 'rb') as f:
            reader = PdfReader(f)
            for page in reader.pages:
                merged_pdf.add_page(page)

with open(f"{target_dir}\\{target_file}", 'wb') as merged_file:
    merged_pdf.write(merged_file)
print("#######################################")
print(f"Successfully merged PDFs from\n\"{source_dir}\" \ninto \n\"{target_dir}\\{target_file}\"")
print("#######################################")
