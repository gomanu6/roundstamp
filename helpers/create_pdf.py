#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint



def create_pdf_from_images(list):
    print("Welcome to Create PDF from Images")

    # pdfs_created = {}



    for dir in list:
        print("Processing ... ", dir)
        # print(os.path.isdir(file))
        # print(file)
        file_name = os.path.basename(dir)
        # pdfs_created[file_name] = []

        doc = fitz.open()
        save_path = os.path.join(dir, file_name)
        list_of_images = os.listdir(dir)
        list_of_images.sort()
        # dpprint(list_of_images)

        for i, f in enumerate(list_of_images):
            # pdfs_created[file_name].append(f)
            img = fitz.open(os.path.join(dir, f))
            rect = img[0].rect
            pdfbytes = img.convert_to_pdf()
            img.close()

            imgPDF = fitz.open("pdf", pdfbytes)
            page = doc.new_page(width = rect.width, height = rect.height)
            page.show_pdf_page(rect, imgPDF, 0)

        doc.save(save_path)
    
    # return pdfs_created




        
        




