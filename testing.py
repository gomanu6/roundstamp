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


def list_files_recursively(directory):
    list_of_files = []

    for path in Path(directory).rglob('*.pdf'):
        
        if path.is_file():
            tmp_lst = []
            tmp_lst.append(str(path))
            tmp_lst.append(str(path).replace(str(unstamped_folder), str(stamped_folder)))

            list_of_files.append(tmp_lst)
            
    return list_of_files


def create_final_paths(files_list):
    print("Creating Final Paths")
    for file in files_list:
        dst_path = file[1]
        Path(dst_path).mkdir(parents=True, exist_ok=True)


a = list_files_recursively(unstamped_folder)
create_final_paths(a)