#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz

stamp_width = 75
stamp_height = 75

dist_right = 150
dist_bottom = 150


def stamp_pdf_page(dir, page, stamp, stamp_width, stamp_height, dist_right, dist_bottom):
    # stamped_pages = {}
    # stamped_pages[dir] = []


    base_dir = os.path.basename(dir)
    page_name = os.path.basename(page)

    print("Stamping File: -->", page_name, " in ", base_dir )
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

    return str(save_path)



def stamp_list_of_pages(list, stamp):

    stamped_pages = []
    
    for item in list:
        file_name = os.path.basename(item)
        dir_path = os.path.dirname(item)

        new_page_name = "st_" + file_name
        save_path = os.path.join(dir_path, new_page_name)

        stamped_page = stamp_pdf_page(dir_path, item, stamp, 75, 75, 100, 100)
        stamped_pages.append(stamped_page)

    return stamped_pages







