#!/usr/bin/env python3

import os
import fitz

print("Hello .. Welcome to the Python Stamp Utility")
print(os.name)

doc = fitz.open("./data/uns_files/books/book-007.pdf")

print("Is this file a pdf file: ", doc.is_pdf)
print("Document Metadata: ", doc.metadata)
print("Document Name: ", doc.name)
print("Document No of Pages: ", doc.page_count)
print("Document Permissions: ", doc.permissions)
print("Document Page Mode: ", doc.pagemode)
print("Document Page Layout: ", doc.pagelayout)
print("Document Needs Password: ", doc.needs_pass)




doc.close()
