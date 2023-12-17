# simple-python-pdf-parser
Whenever I need to do this, it always takes me longer than I want to find and do it. This time I found and tweaked a script to put here.

## pdf_master.py
Use this script to both combine and split PDFs.
Usage:
```
pdf_master.py [-c for combine or -s for split] [input file or dir] [output file or dir]
```
Examples:
```
pdf_master.py -c c:\temp\pdfs\ c:\temp\combo.pdf
pdf_master.py -s c:\temp\big.pdf c:\temp\out\
```
Split can also take a ```base_file_name``` as input, which will be the beginning of the file name, plus a hyphen and the page number.for the file name. 
For example:
```
pdf_master.py -s c:\temp\master.pdf c:\temp\out\ doc
```
Would create files named:
- doc-1.pdf 
- doc-2.pdf



### pdf_combine.py

Use this script to combine your PDFs. Please specify the following (don't forget to escape the backslashes):
- source directory
- target directory
- target file

### pdf_split.py

Use this script to split your PDFs. Please specify the following:
- source file
- target directory
- base name for new files. dash number appended automatically (-1, -2, ..., -99).
  - for example, a base name of 'document' would create files in the specified target_directory named:
    - document-1.pdf
    - document-2.pdf
    - ...
    - document-99.pdf