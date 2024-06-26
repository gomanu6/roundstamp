#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint
import helpers.folder_ops as fo




def convert_single_image_to_pdf(dir, image):
    # print(f"converting {image} to pdf .. ")

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
    os.remove(os.path.join(dir, image))
   
    return save_path




def create_single_pdf_from_list_of_single_images(list):
    print()
    print(" ..... Create Individual PDFs from Images")
    list_of_pdfs_saved = []

    for dir in list:
        print("[STEP 2 of 4]: Processing Images in ... ", dir)

        list_of_images = os.listdir(dir)
        list_of_images.sort()
        
        # list_of_pdfs_saved.append(dir)

        for i, f in enumerate(list_of_images):
            saved_file = convert_single_image_to_pdf(dir, f)
            list_of_pdfs_saved.append(saved_file) ## use for stamp3.py
        
    return list_of_pdfs_saved



def create_pdf_file_from_multiple_images(list):
    print()
    print(" ..... Creating Final Stamped PDF Files ....")

    list_of_folders = fo.get_list_of_unique_folders(list)
    # dpprint(list_of_folders)

    for dir in list_of_folders:
        print()
        print("[STEP 4 of 4]: Processing Image folder ", dir)
        list_of_image_files = os.listdir(dir)
        list_of_image_files.sort()
        # print("List of Images in ", dir)
        # dpprint(list_of_image_files)

        final_doc_name = "st_" + os.path.basename(dir)
        # print("Final File Name ", final_doc_name)
        final_doc_path = os.path.dirname(dir)
        # print("Final file path ", final_doc_path)
        final_doc_save_path = os.path.join(final_doc_path, final_doc_name)
        # print("Final save Path ", final_doc_save_path)

        doc = fitz.open()
        for i, f in enumerate(list_of_image_files):
            img = fitz.open(os.path.join(dir, f))
            rect = img[0].rect
            pdfbytes = img.convert_to_pdf()
            img.close()

            imgpdf = fitz.open("pdf", pdfbytes)
            page = doc.new_page(width = rect.width, height = rect.height)
            page.show_pdf_page(rect, imgpdf, 0)

        doc.save(final_doc_save_path)
        print("Saved Final Stamped PDF File", final_doc_name, "in", final_doc_path)
    
        for item in list_of_image_files:
            os.remove(os.path.join(dir, item))

    for dir in list_of_folders:
        os.rmdir(dir)         
            

        
