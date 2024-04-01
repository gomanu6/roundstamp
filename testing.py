#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import fitz
from pprint import pprint




stamp_file=sys.argv[1]
unstamped_files=sys.argv[2]
stamped_folder=sys.argv[3]
zipped_filename=sys.argv[4]
stamped_files_folder_name=sys.argv[5]
path_to_replace=sys.argv[6]



print(os.listdir(unstamped_files))
print(os.walk(unstamped_files))

files = []
for path, directories, files in os.walk(unstamped_files):
    # print("Path: ", path, "File: ", files)
    for filename in files:
        if filename.endswith(".pdf"):
            print("Path: ", path, "File: ", filename)
            filepath = os.path.join(path, filename)
            print("Filepath: ", filepath)
            files.append(filepath)
    
pprint(files)