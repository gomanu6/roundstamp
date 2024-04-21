#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers import add_numbers as am


# stamp_file=sys.argv[1]
# unstamped_files=sys.argv[2]
# stamped_folder=sys.argv[3]
# zipped_filename=sys.argv[4]
# stamped_files_folder_name=sys.argv[5]
# path_to_replace=sys.argv[6]



# print(os.listdir(unstamped_files))
# print(list(os.walk(unstamped_files)))


print(am.add_nums(3, 4))
