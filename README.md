# simple-python-pdf-parser
Whenever I need to do this, it always takes me longer than I want to find and do it. This time I found and tweaked a script to put here.

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