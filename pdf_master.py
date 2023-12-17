# pdf_master.py
from PyPDF2 import PdfReader, PdfWriter
import os
import sys

## c for combine, s for split
if '-c' in sys.argv:
    action = 'combine'
    sys.argv.remove('-c')
elif '-s' in sys.argv:
    action = 'split'
    sys.argv.remove('-s')
else:
    print("Invalid action. Please use either -c for 'combine' or -s for 'split'.")
    exit()

if action == "combine":
    ## first variable is the source, second is the destination
    source_dir = sys.argv[1]
    target_file = sys.argv[2]
    merged_pdf = PdfWriter()

    for filename in os.listdir(source_dir):
        if filename.endswith(".pdf"):
            print(f"Combining: {filename}")
            absolute_path = os.path.join(source_dir, filename)
            with open(absolute_path, 'rb') as f:
                reader = PdfReader(f)
                for page in reader.pages:
                    merged_pdf.add_page(page)

    with open(f"{target_file}", 'wb') as merged_file:
        merged_pdf.write(merged_file)
    print("#######################################")
    print(f"Successfully merged PDFs from:\n    \"{source_dir}\"\ninto:\n    \"{target_file}\"")
    print("#######################################")

elif action == "split":
    ## first variable is the source, second is the destination
    ## third if present is the base file name, otherwise we default to 'page'
    source_file = sys.argv[1]
    target_dir = sys.argv[2]
    base_name = "page" if len(sys.argv) < 4 else sys.argv[3]

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
    
    count-=1
    print("#######################################")
    print(f"Finished splitting: {source_file} into {count} pages.")
    print("#######################################")

else:
    print("Something went wrong.")
    exit()
