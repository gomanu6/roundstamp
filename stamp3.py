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
from helpers.create_pdf_of_image import create_pdf_of_image as cpi


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

cpi(p)
# cpfi(p)