#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint
import helpers.file_inventory as fi



def create_pixmap_from_single_pdf(document):

    doc = fitz.open(document)
    matrix = fitz.Matrix(2, 2)

    old_doc_name = os.path.basename(document)
    dir_path = os.path.dirname(document)
    dir_name = os.path.basename(dir_path)

    new_doc_name = str(old_doc_name).replace(".pdf", ".png")

    for page in doc:
        pix = page.get_pixmap(matrix=matrix)
        image_path = os.path.join(dir_path, new_doc_name)
        pix.save(image_path)
    



def create_pixmaps(src_dir, dst_dir):
    print("Welcome to Creating Pixmaps ....")
    final_list = fi.create_filtered_src_dst_files(src_dir, dst_dir)

    list_of_pixmaps = []

    for file in final_list:
        
        src_file = file[0]
        dst_file = file[1]
        list_of_pixmaps.append(dst_file)
        Path(dst_file).mkdir(parents=True, exist_ok=True)

        print("Processing ", src_file)


        doc = fitz.open(src_file)
        matrix = fitz.Matrix(2, 2)    

        for page in doc:
            pix = page.get_pixmap(matrix=matrix)
            img_filename = "page-%06i.png" % (page.number)
            img_path = os.path.join(dst_file, img_filename)
            pix.save(img_path)
    

        doc.close()

    return list_of_pixmaps



def create_pixmap_from_list(list):

    
    list_of_pixmaps = []

    for item in list:
        doc_name = os.path.basename(item)
        dir_path = os.path.dirname(item)

        new_pix_name = str(doc_name).replace(".pdf", ".png")

        doc = fitz.open(item)
        matrix = fitz.Matrix(2, 2)
        print("Creating pixmap for : ", doc_name, " in ", os.path.basename(dir_path))
        for page in doc:
            pix = page.get_pixmap(matrix=matrix)
            save_path = os.path.join(dir_path, new_pix_name)
            pix.save(save_path)
            list_of_pixmaps.append(save_path)
        
        os.remove(item)
        
    return list_of_pixmaps
        





