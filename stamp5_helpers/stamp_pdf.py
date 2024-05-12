#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz


stamp_width = 80
stamp_height = 80

dist_right = 150
dist_bottom = 100

matrix=fitz.Matrix(1,1)


def stamp_pdf_page(working_dir, pagename, stamp, stamp_width, stamp_height, dist_right, dist_bottom):

    old_page = os.path.join(working_dir, pagename)
    doc = fitz.open(old_page)

    for open_page in doc:
        page_width = open_page.rect.width
        page_height = open_page.rect.height

        start_width = (page_width - dist_right)
        start_height = (page_height - dist_bottom)

        end_width = start_width + stamp_width
        end_height = start_height + stamp_height
    
        coords = fitz.Rect(start_width, start_height, end_width, end_height)

        open_page.insert_image(coords, filename=stamp)

        pix = open_page.get_pixmap(matrix=matrix)
        img_name = "st_" + str(pagename).replace(".pdf", ".png")
        pix_save_path = os.path.join(working_dir, img_name)
        pix.save(pix_save_path)
    
    doc.close()
    os.remove(old_page)
    return str(img_name)



def stamp_list_of_pages(all_files, stamp):

    for key in all_files:
        working_path = all_files[key]["working_path"]
        unstamped_pdf_files = all_files[key]["unstamped_pdf_files"]
        stamped_pages = []

        for file in unstamped_pdf_files:
                stamped_page = stamp_pdf_page(working_path, file, stamp, stamp_width, stamp_height, dist_right, dist_bottom)
                stamped_pages.append(stamped_page)
        
        all_files[key]["unstamped_pdf_files"] = []
        all_files[key]["stamped_images"] = stamped_pages

            

