#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.dpprint import dpprint

import helpers.file_inventory as fi
import helpers.create_pixmaps as cpx


stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
stamped_folder = sys.argv[3]
pixmaps_folder = sys.argv[4]


a = fi.create_filtered_src_dst_files(unstamped_folder, stamped_folder)
# dpprint(a)

b = cpx.create_initial_pixmaps_from_list(a)
dpprint(b)

