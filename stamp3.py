#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.create_filtered_files_list import create_filtered_files_list




stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
stamped_folder = sys.argv[3]
images_folder = sys.argv[4]

# file_list = os.listdir(unstamped_folder)
# file_list.sort()
# pprint(file_list)


