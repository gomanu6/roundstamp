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
import helpers.stamp_pdf as sp

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

p = cp.create_pixmaps(unstamped_folder, pixmaps_folder)
# dpprint(p)

z = cpi(p)

x = sp.stamp_list_of_pages(z, stamp_file)

# dpprint(x)

y = cp.create_pixmap_from_list(x)
dpprint(y)

# # stamped_pdfs = {}
# for item in z:
#     file_name = os.path.basename(item)
#     dir_path = os.path.dirname(item)
#     # print("Dir Name: -- ", dir_name)
#     new_page_name = "st_" + file_name
#     # print("new page name is : ", new_page_name)
#     save_path = os.path.join(dir_path, new_page_name)
#     # print("Save Path : ", save_path)
    
#     # pdf_name = os.path.basename(dir_path)
#     stamped_pages = []
#     # stamped_pdfs[pdf_name] = {}
#     # stamped_pdfs[pdf_name][dir_path] = dir_path


#     stamped_page = spp(dir_path, item, stamp_file, 75, 75, 100, 100)
#     stamped_pages.append(stamped_page)

#     stamped_pages
#     # print("The file is : -->", item)
#     # print("The dirname is: -->", os.path.dirname(item))

# # {
# # "book_name" : "name of book",
# # "path" : "dir path"
# # "pages" : [page, page]
# # }

