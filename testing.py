#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import fitz
from pprint import pprint

from helpers import add_numbers as am


stamp_file=sys.argv[1]
unstamped_folder=sys.argv[2]
stamped_folder=sys.argv[3]
images_folder=sys.argv[4]


# zipped_filename=sys.argv[4]


