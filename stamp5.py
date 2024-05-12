#!/usr/bin/env python3


import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers.dpprint import dpprint

import stamp5_helpers.filer_list as fl
import stamp5_helpers.pixmaps as pm
import stamp5_helpers.pdf as pd
import stamp5_helpers.stamp_pdf as sp

stamp_file = sys.argv[1]
print("Stamp File is: ", stamp_file)
unstamped_folder = sys.argv[2]
working_folder = sys.argv[3]
stamped_folder = sys.argv[4]


all_files = fl.create_filtered_files(unstamped_folder, working_folder, stamped_folder)

pm.create_pixmaps(all_files)
pd.convert_list_of_images_to_pdf(all_files)
sp.stamp_list_of_pages(all_files, stamp_file)

dpprint(all_files)



