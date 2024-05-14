#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint
import time

from helpers.dpprint import dpprint

import stamp6_helpers.filer_list as fl
import stamp6_helpers.pixmaps as pm
import stamp6_helpers.pdf as pd
import stamp6_helpers.stamp_pdf as sp

stamp_file = sys.argv[1]
# print("Stamp File is: ", stamp_file)
unstamped_folder = sys.argv[2]
working_folder = sys.argv[3]
stamped_folder = sys.argv[4]


stamp_width = 60
stamp_height = 60

dist_right = 150
dist_bottom = 100

pixmap_matrix=fitz.Matrix(5,5)
stamp_matrix=fitz.Matrix(5,5)



all_files = fl.create_filtered_files(unstamped_folder, working_folder, stamped_folder)

## Stamp 5 Way
# pm.create_pixmaps(all_files)
# pd.convert_list_of_images_to_pdf(all_files)
# sp.stamp_list_of_pages(all_files, stamp_file)
# sp.create_pdf(all_files)


## Stamp 6 Way
total_files = len(all_files)
total_pages = 0

for index, key in enumerate(all_files):
    file_start_time = time.time()
    filepath = all_files[key]["filepath"]
    working_dir = all_files[key]["working_path"]
    filename = all_files[key]["filename"]
    final_path = all_files[key]["dst_path"]


    ### Create Pixmaps
    print()
    print(f"Processing File {index + 1} of {total_files}", "File:", filename, "in ", os.path.basename(os.path.dirname(filepath)))
    pixmap_start_time = time.time()
    file_pixmaps = pm.create_pixmap_of_pdf(filepath, working_dir, matrix=pixmap_matrix)
    all_files[key]["pixmap_pages"] = file_pixmaps
    num_pages = len(all_files[key]["pixmap_pages"])
    print(f"  -- This file has {num_pages} Pages")
    pixmap_end_time = time.time()
    pixmap_time_taken = pixmap_end_time - pixmap_start_time
    print(f"       |__ that took {str(round(pixmap_time_taken, 2))} seconds")
    
    ### Convert Pixmap to PDF
    pixmap_files = all_files[key]["pixmap_pages"]
    unstamped_pdf_files = []
    print("    Converting Pixmaps to pdf files")
    pix_pdf_start_time = time.time()
    for pix_file in pixmap_files:
        pdf_file = pd.convert_image_to_pdf(pix_file, working_dir)
        unstamped_pdf_files.append(pdf_file)
        total_pages += 1
    all_files[key]["pixmap_pages"] = []
    all_files[key]["unstamped_pdf_files"] = unstamped_pdf_files
    pix_pdf_end_time = time.time()
    pix_pdf_time = pix_pdf_end_time - pix_pdf_start_time
    print(f"       |__ that took {str(round(pix_pdf_time, 2))} seconds")


    ### Stamp PDF Files and convert to Pixmaps
    unstamped_pdf_files = all_files[key]["unstamped_pdf_files"]
    stamped_pages = []
    print("    Stamping PDF files")
    stamp_start_time = time.time()
    for unstamped_file in unstamped_pdf_files:
        stamped_page = sp.stamp_pdf_page(working_dir, unstamped_file, stamp_file, stamp_width, stamp_height, dist_right, dist_bottom, stamp_matrix)
        stamped_pages.append(stamped_page)
    all_files[key]["unstamped_pdf_files"] = []
    all_files[key]["stamped_images"] = stamped_pages
    stamp_end_time = time.time()
    stamp_time = stamp_end_time - stamp_start_time
    print(f"       |__ that took {str(round(stamp_time, 2))} seconds")


    ### Create final pdf files
    Path(final_path).mkdir(parents=True, exist_ok=True)
    stamped_images = all_files[key]["stamped_images"]
    stamped_images.sort()
    print("    Creating final stamped PDF File")
    final_pdf_start_time = time.time()
    doc = fitz.open()
    for file in stamped_images:
        img = fitz.open(os.path.join(working_dir, file))
        rect = img[0].rect
        pdfbytes = img.convert_to_pdf()
        img.close()

        imgpdf = fitz.open("pdf", pdfbytes)
        page = doc.new_page(width = rect.width, height = rect.height)
        page.show_pdf_page(rect, imgpdf, 0)
    
    doc.save(final_path)
    all_files[key]["stamped_images"] = []
    final_pdf_end_time = time.time()
    final_pdf_time = final_pdf_end_time - final_pdf_start_time
    print(f"       |__ that took {str(round(final_pdf_time, 2))} seconds")

    file_end_time = time.time()
    file_time = file_end_time - file_start_time
    uom = "seconds"
    reported_time = file_time / 60
    if file_time > 60:
        uom = "minutes"
        print(f"  |--- File {index + 1} took {str(round(reported_time, 2))} {uom}")
    else:
        print(f"  |--- File {index + 1} took {str(round(file_time, 2))} seconds")


print()
print("Total Files Stamped: ", total_files)
print("Total Pages stamped: ", total_pages)
# print("Thank you for using the Stamping Utility")
# dpprint(all_files)


