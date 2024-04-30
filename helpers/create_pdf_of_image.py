#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint




def convert_single_image_to_pdf(dir, image):
    print(f"converting {image} to pdf .. ")

    doc = fitz.open()
    s = str(image).replace(".png", ".pdf")

    img = fitz.open(os.path.join(dir, image))
    rect = img[0].rect
    pdfbytes = img.convert_to_pdf()
    img.close()

    imgpdf = fitz.open("pdf", pdfbytes)
    page = doc.new_page(width = rect.width, height = rect.height)
    page.show_pdf_page(rect, imgpdf, 0)
    save_path = os.path.join(dir, s)

    doc.save(save_path)
   
    return save_path




def create_pdf_from_list_of_images(list):

    print("Welcome to Create PDF from list of Images")
    list_of_pdfs_saved = []
    for dir in list:
        print()
        print("Processing ... ", dir)
        # print(os.path.isdir(file))
        # print(file)

        # save_path = os.path.join(dir, os.path.basename(dir))
        list_of_images = os.listdir(dir)
        list_of_images.sort()
        # dpprint(list_of_images)

        for i, f in enumerate(list_of_images):
            saved_file = convert_single_image_to_pdf(dir, f)
            list_of_pdfs_saved.append(saved_file)
        
    return list_of_pdfs_saved









