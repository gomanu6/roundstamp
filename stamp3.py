#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.dpprint import dpprint
import helpers.file_inventory as fi
import helpers.folder_ops as fo
import helpers.pdf_info as gpi
import helpers.create_pixmaps as cp
from helpers.create_pdf import create_pdf_from_images as cpfi
from helpers.create_pdf_of_image import create_pdf_from_list_of_images as cpi
from helpers.stamp_pdf import stamp_pdf_page as spp


stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
stamped_folder = sys.argv[3]
pixmaps_folder = sys.argv[4]

# file_list = os.listdir(unstamped_folder)
# file_list.sort()
# pprint(file_list)
a = fi.create_filtered_files(unstamped_folder)
# dpprint(a)

# b = fi.create_filtered_src_dst_files(unstamped_folder, stamped_folder)
# dpprint(b)

# dpprint(create_filtered_src_dst_files(unstamped_folder, stamped_folder))
# dpprint(create_filtered_dst_files(unstamped_folder, stamped_folder))


# b = fi.create_filtered_unique_dst_folder(unstamped_folder, stamped_folder)

# fo.create_folders_from_list(b)

# for item in a:
#     dpprint(gpi.get_file_info(item, "name", "is_pdf", "is_encrypted", "page_count", "version_count"))

p = cp.create_pixmaps(a, unstamped_folder, pixmaps_folder, stamp_file)
# dpprint(p)

z = cpi(p)

for item in z:
    file_name = os.path.basename(item)
    dir_name = os.path.dirname(item)
    # print("Dir Name: -- ", dir_name)
    new_page_name = "st_" + file_name
    # print("new page name is : ", new_page_name)
    save_path = os.path.join(dir_name, new_page_name)
    # print("Save Path : ", save_path)

    spp(dir_name, item, stamp_file, 75, 75, 100, 100)
    # print("The file is : -->", item)
    # print("The dirname is: -->", os.path.dirname(item))

