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

import helpers.create_pdf_of_image as cpi
import helpers.stamp_pdf as sp

stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
stamped_folder = sys.argv[3]
pixmaps_folder = sys.argv[4]
# print(pixmaps_folder)


# a = fi.create_filtered_files(unstamped_folder)
# dpprint(a)

# b = fi.create_filtered_src_dst_files(unstamped_folder, stamped_folder)
# dpprint(b)

# dpprint(create_filtered_src_dst_files(unstamped_folder, stamped_folder))
# dpprint(create_filtered_dst_files(unstamped_folder, stamped_folder))


# b = fi.create_filtered_unique_dst_folder(unstamped_folder, stamped_folder)

# fo.create_folders_from_list(b)

# for item in a:
#     dpprint(gpi.get_file_info(item, "name", "is_pdf", "is_encrypted", "page_count", "version_count"))


### Create a Second order list with source and destination paths to pdf files
a = fi.create_filtered_src_dst_files(unstamped_folder, stamped_folder)
# dpprint(a)

### Create individual Pixmaps from PDF Files
b = cp.create_initial_pixmaps_from_list(a)
# dpprint(b)

### Convert pixmaps to individual PDF files to prepare for stamping
z = cpi.create_single_pdf_from_list_of_single_images(b)
dpprint(z)

### Stamp individual PDF Files
x = sp.stamp_list_of_pages(z, stamp_file)
# dpprint(x)

### Create Pixmaps of stamped PDF Files
y = cp.create_pixmap_from_list(x)
# dpprint(y)

### Convert and collate stamped pixmaps into final PDF Files
a = cpi.create_pdf_file_from_multiple_images(y)

