#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint
import time
import logging

from helpers.dpprint import dpprint

import stamp8_helpers.filer_list as fl
import stamp8_helpers.pixmaps as pm
import stamp8_helpers.pdf as pd
import stamp8_helpers.stamp_pdf as sp
import stamp8_helpers.general as gen


logging.basicConfig(filename="log.txt", force=True, filemode="a", level=logging.DEBUG, format='%(levelname)s:%(message)s')

stamp_file = sys.argv[1]
# print("Stamp File is: ", stamp_file)
unstamped_folder = sys.argv[2]
working_folder = sys.argv[3]
stamped_folder = sys.argv[4]


stamp_width = 120
stamp_height = 120

dist_right = 140
dist_bottom = 150

pixmap_matrix=fitz.Matrix(2,2)
stamp_matrix=fitz.Matrix(2,2)

INDIVIDUAL_PROCESS_TIME = True
# PYTHON_SCRIPT_TIME = True

# py_start_time = time.time()

pdf_files, protected_files = fl.create_filtered_files(unstamped_folder, working_folder, stamped_folder)
# pprint(pdf_files)
# pprint(unoperated_files)

# protected_files = fl.analyse_files(pdf_files)
# pprint(protected_files)

unprocessed_files = fl.files_not_processed(unstamped_folder)
# sys.exit()


## Stamp 5 Way
# pm.create_pixmaps(pdf_files)
# pd.convert_list_of_images_to_pdf(pdf_files)
# sp.stamp_list_of_pages(pdf_files, stamp_file)
# sp.create_pdf(pdf_files)

logging.debug(f"-------{sys.argv[0]}-------")
logging.debug("Debug Info: ")
logging.debug("Initial Pixmap Matrix: {pixmap_matrix}")
logging.debug("Stamp Pixmap Matrix: {stamp_matrix}")

# sys.exit()

## Stamp 8 Way
total_files = len(pdf_files)
total_pages = 0




pixmap_time = 0
pixmap_to_pdf_time = 0
total_stamp_time = 0
total_final_pdf_time = 0
total_time = 0


files_with_errors = {}

for index, key in enumerate(pdf_files):
    file_start_time = time.time()
    filepath = pdf_files[key]["filepath"]
    working_dir = pdf_files[key]["working_path"]
    filename = pdf_files[key]["filename"]
    final_path = pdf_files[key]["dst_path"]


    ### Create Pixmaps
    print()
    print(f"Processing File {index + 1} of {total_files}", "File:", filename, "in ", os.path.basename(os.path.dirname(filepath)))
    pixmap_start_time = time.time()
    try:
        file_pixmaps = pm.create_pixmap_of_pdf(filepath, working_dir, matrix=pixmap_matrix)
    except Exception as e:
        # files_with_errors.append(filepath)
        files_with_errors[filepath] = e
        print("--- ERROR --- Unable to Open File for creating Pixmaps")
        continue
    pdf_files[key]["pixmap_pages"] = file_pixmaps
    num_pages = len(pdf_files[key]["pixmap_pages"])
    print(f"  -- This file has {num_pages} Pages")
    pixmap_end_time = time.time()
    gen.report_time("       |__ Created Pixmaps in ---", pixmap_start_time, pixmap_end_time, report_time = INDIVIDUAL_PROCESS_TIME)
    # pixmap_time_taken = pixmap_end_time - pixmap_start_time
    # pixmap_time += pixmap_time_taken
    total_time += pixmap_time
    # print(f"       |__ Created Pixmaps --- {str(round(pixmap_time_taken, 2))} seconds")
    
    ### Convert Pixmap to PDF
    pixmap_files = pdf_files[key]["pixmap_pages"]
    unstamped_pdf_files = []
    # print("    Converting Pixmaps to pdf files")
    pix_pdf_start_time = time.time()
    for pix_file in pixmap_files:
        pdf_file = pd.convert_image_to_pdf(pix_file, working_dir)
        unstamped_pdf_files.append(pdf_file)
        total_pages += 1
    pdf_files[key]["pixmap_pages"] = []
    pdf_files[key]["unstamped_pdf_files"] = unstamped_pdf_files
    pix_pdf_end_time = time.time()
    pix_pdf_time = pix_pdf_end_time - pix_pdf_start_time
    pixmap_to_pdf_time += pix_pdf_time
    print(f"       |__ Converted Pixmaps to pdf files --- {str(round(pix_pdf_time, 2))} seconds")


    ### Stamp PDF Files and convert to Pixmaps
    unstamped_pdf_files = pdf_files[key]["unstamped_pdf_files"]
    stamped_pages = []
    # print("    Stamping PDF files")
    stamp_start_time = time.time()
    for unstamped_file in unstamped_pdf_files:
        stamped_page = sp.stamp_pdf_page(working_dir, unstamped_file, stamp_file, stamp_width, stamp_height, dist_right, dist_bottom, stamp_matrix)
        stamped_pages.append(stamped_page)
    pdf_files[key]["unstamped_pdf_files"] = []
    pdf_files[key]["stamped_images"] = stamped_pages
    stamp_end_time = time.time()
    stamp_time = stamp_end_time - stamp_start_time
    total_stamp_time += stamp_time
    print(f"       |__ Stamped PDF Files --- {str(round(stamp_time, 2))} seconds")


    ### Create final pdf files
    Path(final_path).mkdir(parents=True, exist_ok=True)
    stamped_images = pdf_files[key]["stamped_images"]
    stamped_images.sort()
    # print("    Creating final stamped PDF File")
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
    pdf_files[key]["stamped_images"] = []
    final_pdf_end_time = time.time()
    final_pdf_time = final_pdf_end_time - final_pdf_start_time
    total_final_pdf_time += final_pdf_time
    print(f"       |__ Created Final PDF File --- {str(round(final_pdf_time, 2))} seconds")

    file_end_time = time.time()
    file_time = file_end_time - file_start_time
    uom = "seconds"
    reported_time = file_time
    if file_time > 60:
        uom = "minutes"
        reported_time = file_time / 60
        print(f"  |--- File {index + 1} took {str(round(reported_time, 2))} {uom}")
    else:
        print(f"  |--- File {index + 1} took {str(round(reported_time, 2))} {uom}")


total_time += pixmap_to_pdf_time
total_time += total_stamp_time
total_time += total_final_pdf_time


def get_uom(time):
    uom = "seconds"
    reported_time = str(round(time, 2))
    if time > 60:
        uom = "minutes"
        reported_time = str(round(time / 60, 2))
    return [reported_time, uom]


print()
print("Total Files Stamped: ", total_files)
print("Total Pages stamped: ", total_pages)
print()
# print("Total Pixmap Time: ", get_uom(pixmap_time)[0], get_uom(pixmap_time)[1])
# print("Total Pixmap to PDF Time: ", get_uom(pixmap_to_pdf_time)[0], get_uom(pixmap_to_pdf_time)[1])
# print("Total Stamping Time: ", get_uom(total_stamp_time)[0], get_uom(total_stamp_time)[1])
# print("Total Final PDF Time: ", get_uom(total_final_pdf_time)[0], get_uom(total_final_pdf_time)[1])


### Printing Files with Errors
if files_with_errors:
    print()
    print("----- Following files with errors ----")
    for index, file in enumerate(files_with_errors):
        print(int(index + 1), "--", file, "-->", files_with_errors[file])
    # pprint(files_with_errors)
    print("----- End of files with errors ----")
    print()

py_report_uom, py_report_time = get_uom(total_time)
# py_report_time = str(round(total_time, 2))

if total_time > 60:
    py_report_uom = "minutes"
    py_report_time = str(round(total_time / 60, 2))

print("Total Time Taken by Python = ", py_report_time, py_report_uom)
# print("Thank you for using the Stamp 6 Utility")
# dpprint(pdf_files)


