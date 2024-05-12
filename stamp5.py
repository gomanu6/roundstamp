#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.dpprint import dpprint

import stamp5_helpers.filer_list as fl
import stamp5_helpers.pixmaps as pm

stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
working_folder = sys.argv[3]
stamped_folder = sys.argv[4]


all_files = fl.create_filtered_files(unstamped_folder, working_folder, stamped_folder)

pm.create_pixmaps(all_files)

