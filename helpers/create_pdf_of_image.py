#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint


def create_pdf_of_image(list):
    print("Welcome to Create PDF of Image")
    for dir in list:
        print("Processing ... ", dir)
        # print(os.path.isdir(file))
        # print(file)

        # save_path = os.path.join(dir, os.path.basename(dir))
        list_of_images = os.listdir(dir)
        list_of_images.sort()
        # dpprint(list_of_images)

        for i, f in enumerate(list_of_images):
            doc = fitz.open()
            s = str(f).replace(".png", ".pdf")
            
            img = fitz.open(os.path.join(dir, f))
            rect = img[0].rect
            pdfbytes = img.convert_to_pdf()
            img.close()

            imgPDF = fitz.open("pdf", pdfbytes)
            page = doc.new_page(width = rect.width, height = rect.height)
            page.show_pdf_page(rect, imgPDF, 0)
            save_path = os.path.join(dir, s)

            doc.save(save_path)











