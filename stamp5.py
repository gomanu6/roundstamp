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
import helpers.stamp_pdf as sp


stamp_file = sys.argv[1]
unstamped_folder = sys.argv[2]
stamped_folder = sys.argv[3]
pixmaps_folder = sys.argv[4]






