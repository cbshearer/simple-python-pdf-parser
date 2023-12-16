# pdf_splitter.py
from PyPDF2 import PdfReader, PdfWriter
#myPDF = "file.pdf"
myPDF = "C:\\temp\\file.pdf"
with open(myPDF, 'rb') as infile:
    reader = PdfReader(infile)
    count = 1
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
        page_name = f"output-{count}.pdf"
        print(f"Splitting page {count} to file {page_name}")
        with open(page_name, 'wb') as outfile:
            writer.write(outfile)
            writer = PdfWriter()
        count+=1
print("#######################################")
print(f"Finished processing: {myPDF}")
print("#######################################")
