#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint

matrix_x = 1
matrix_y = 1


def create_pixmap_of_pdf(src_file, working_folder):
    
    list_of_pixmaps = []

    Path(working_folder).mkdir(parents=True, exist_ok=True)

    print("Processing ", src_file)

    doc = fitz.open(src_file)
    matrix = fitz.Matrix(matrix_x, matrix_y) 

    for page in doc:
        pix = page.get_pixmap(matrix=matrix)
        img_filename = "page-%06i.png" % (page.number)
        img_path = os.path.join(working_folder, img_filename)
        pix.save(img_path)
        list_of_pixmaps.append(img_filename)
    doc.close()

    return list_of_pixmaps


def create_pixmaps(all_files):

    for key in all_files:
        src_dir = all_files[key]["filepath"]
        dst_dir = all_files[key]["working_path"]

        pixmaps = create_pixmap_of_pdf(src_dir, dst_dir)

        all_files[key]["pixmap_pages"] = pixmaps
        

