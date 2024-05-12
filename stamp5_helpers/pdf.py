#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint




def convert_image_to_pdf(image, working_dir):
    src_path = os.path.join(working_dir, image)
    doc = fitz.open()
    pdf_file_name = str(image).replace(".png", ".pdf")

    img = fitz.open(os.path.join(working_dir, image))
    rect = img[0].rect
    pdfbytes = img.convert_to_pdf()
    img.close()

    imgpdf = fitz.open("pdf", pdfbytes)
    page = doc.new_page(width = rect.width, height = rect.height)
    page.show_pdf_page(rect, imgpdf, 0)
    save_path = os.path.join(working_dir, pdf_file_name)

    doc.save(save_path)
    os.remove(os.path.join(working_dir, image))
    # os.remove(src_path)
    # print(os.path.join(working_dir, image))
   
    return pdf_file_name



def convert_list_of_images_to_pdf(all_files):

    for key in all_files:
        working_path = all_files[key]["working_path"]
        pixmap_files = all_files[key]["pixmap_pages"]
        unstamped_pdf_files = []

        for file in pixmap_files:
            pdf_file = convert_image_to_pdf(file, working_path)
            unstamped_pdf_files.append(pdf_file)
        
        all_files[key]["pixmap_pages"] = []
        all_files[key]["unstamped_pdf_files"] = unstamped_pdf_files





