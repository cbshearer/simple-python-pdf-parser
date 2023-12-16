# pdf_split.py
from PyPDF2 import PdfReader, PdfWriter


source_file = "c:\\users\\chris\\big.pdf"
target_dir = "c:\\temp\\pdf"
base_name = "page"

with open(source_file, 'rb') as infile:
    reader = PdfReader(infile)
    count = 1
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
        page_name = f"{target_dir}\\{base_name}-{count}.pdf"
        print(f"Splitting page {count} to file {page_name}")
        with open(page_name, 'wb') as outfile:
            writer.write(outfile)
            writer = PdfWriter()
        count+=1
print("#######################################")
print(f"Finished processing: {source_file}")
print("#######################################")
