#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.dpprint import dpprint
import helpers.file_inventory as fi


stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
stamped_folder = sys.argv[3]
images_folder = sys.argv[4]

# file_list = os.listdir(unstamped_folder)
# file_list.sort()
# pprint(file_list)
# a = create_filtered_files(unstamped_folder)
# dpprint(a)

# dpprint(create_filtered_src_dst_files(unstamped_folder, stamped_folder))
# dpprint(create_filtered_dst_files(unstamped_folder, stamped_folder))


b = fi.create_filtered_unique_dst_folder(unstamped_folder, stamped_folder)
dpprint(b)
