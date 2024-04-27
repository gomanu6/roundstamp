#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz



def stamp_pixmap(directory):
    fname = os.path.basename(directory)
    print(fname)
    doc = fitz.open()
    for img in os.listdir(directory):
        pix = fitz.Pixmap(img)
        imgpdf = fitz.open("pdf", pix.pdfocr_tobytes())
        doc.insert_pdf(imgpdf)
        pix = None
        imgpdf.close()
    doc.save("ocr-images.pdf")




