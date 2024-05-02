#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.dpprint import dpprint

import helpers.file_inventory as fi
import helpers.create_pixmaps as cpx
import helpers.create_pdf_of_image as cpi


stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
stamped_folder = sys.argv[3]
pixmaps_folder = sys.argv[4]

### Create a Second order list with source and destination paths to pdf files
a = fi.create_filtered_src_dst_files(unstamped_folder, stamped_folder)
# dpprint(a)

### Create individual Pixmaps from PDF Files
b = cpx.create_initial_pixmaps_from_list(a)
dpprint(b)

### Convert Pixmap files back to PDF files prior to Stamping
c = cpi.create_single_pdf_from_list_of_single_images(b)
dpprint(c)
