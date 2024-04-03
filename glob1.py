#!/usr/bin/env python3

import os
import sys
# from pathlib import Path
import fitz
from pprint import pprint




stamp_file=sys.argv[1]
unstamped_files=sys.argv[2]
stamped_folder=sys.argv[3]
zipped_filename=sys.argv[4]
stamped_files_folder_name=sys.argv[5]
path_to_replace=sys.argv[6]
stamped_folder_name=sys.argv[7]

# print(stamp_file)
# print(unstamped_files)
# print(stamped_folder)
# print(zipped_filename)
# print(stamped_files_folder_name)
# print(path_to_replace)

import pathlib

def list_files_recursively(directory):
    list_of_files = []

    for path in pathlib.Path(directory).rglob('*.pdf'):
        
        if path.is_file():
            tmp_lst = []
            unchanged_part = list(path.parts)
            tmp_lst.append(unchanged_part)

            changed_part = list(path.parts)
            changed_part[1] = stamped_folder_name
            tmp_lst.append(changed_part)

            list_of_files.append(tmp_lst)
            
    return list_of_files

a = list_files_recursively(unstamped_files)
pprint(a)


# def get_final_paths(path):
#     final_paths = []

#     for path in path:
#         path[1]  = "st_files"
#         final_paths.append(path)
    
#     return final_paths


# b = get_final_paths(a)
# # pprint(b)


# def final_list(list):
#     final_list = []

#     for path in list:
#         tmp_lst = []
#         # src = path
#         # dst = get_final_paths(src)
#         # tmp_lst.append(src)
#         # tmp_lst.append(dst)
#         print(path)

#         # final_list.append(tmp_lst)
    
#     return final_list

# c = final_list(a)
# print(c)




