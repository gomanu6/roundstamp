#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.dpprint import dpprint

import stamp5_helpers.filer_list as fl
import stamp5_helpers.pixmaps as pm
import stamp5_helpers.pdf as pd
import stamp5_helpers.stamp_pdf as sp

stamp_file = sys.argv[1]
# print("Stamp File is: ", stamp_file)
unstamped_folder = sys.argv[2]
working_folder = sys.argv[3]
stamped_folder = sys.argv[4]


stamp_width = 80
stamp_height = 80

dist_right = 150
dist_bottom = 100

matrix=fitz.Matrix(2,2)



all_files = fl.create_filtered_files(unstamped_folder, working_folder, stamped_folder)

# pm.create_pixmaps(all_files)
# pd.convert_list_of_images_to_pdf(all_files)
# sp.stamp_list_of_pages(all_files, stamp_file)
# sp.create_pdf(all_files)


# for i, key in enumerate(all_files):
#     print(i)
#     print(key)

total_files = len(all_files)
total_pages = 0

for index, key in enumerate(all_files):
    filepath = all_files[key]["filepath"]
    working_dir = all_files[key]["working_path"]
    filename = all_files[key]["filename"]
    final_path = all_files[key]["dst_path"]


    ### Create Pixmaps
    print()
    print(f"Processing File {index + 1} of {total_files}")
    # print(f"Processing File {index + 1} of {total_files}", filename, "in ", os.path.dirname(filepath))
    file_pixmaps = pm.create_pixmap_of_pdf(filepath, working_dir)
    all_files[key]["pixmap_pages"] = file_pixmaps
    
    ### Convert Pixmap to PDF
    pixmap_files = all_files[key]["pixmap_pages"]
    unstamped_pdf_files = []
    print("    Converting Pixmaps to pdf files")
    for pix_file in pixmap_files:
        pdf_file = pd.convert_image_to_pdf(pix_file, working_dir)
        unstamped_pdf_files.append(pdf_file)
        total_pages += 1
    all_files[key]["pixmap_pages"] = []
    all_files[key]["unstamped_pdf_files"] = unstamped_pdf_files


    ### Stamp PDF Files and convert to Pixmaps
    unstamped_pdf_files = all_files[key]["unstamped_pdf_files"]
    stamped_pages = []
    print("    Stamping PDF files")
    for unstamped_file in unstamped_pdf_files:
        stamped_page = sp.stamp_pdf_page(working_dir, unstamped_file, stamp_file, stamp_width, stamp_height, dist_right, dist_bottom)
        stamped_pages.append(stamped_page)
    all_files[key]["unstamped_pdf_files"] = []
    all_files[key]["stamped_images"] = stamped_pages


    ### Create final pdf files
    Path(final_path).mkdir(parents=True, exist_ok=True)
    stamped_images = all_files[key]["stamped_images"]
    stamped_images.sort()
    print("    Creating final stamped PDF File")
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

print()
print("Total Files Stamped: ", total_files)
print("Total Pages stamped: ", total_pages)
# print("Thank you for using the Stamping Utility")
# dpprint(all_files)


