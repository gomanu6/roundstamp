#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz

stamp_width = 75
stamp_height = 75

dist_right = 100
dist_bottom = 100

def stamp_pdf_page(dir, page, stamp, stamp_width, stamp_height, dist_right, dist_bottom):
    print("Stamping File: -->", os.path.basename(page), " in ", os.path.basename(dir) )
    # open_path = os.path.join(dir, page)
    old_page = page

    doc = fitz.open(page)
    new_name = "st_" + str(os.path.basename(page))
    save_path = os.path.join(dir, new_name)

    for page in doc:
        page_width = page.rect.width
        page_height = page.rect.height

        start_width = (page_width - dist_right)
        start_height = (page_height - dist_bottom)

        end_width = start_width + stamp_width
        end_height = start_height + stamp_height
    
        coords = fitz.Rect(start_width, start_height, end_width, end_height)

        page.insert_image(coords, filename=stamp)
    
    doc.ez_save(save_path)

    os.remove(old_page)






