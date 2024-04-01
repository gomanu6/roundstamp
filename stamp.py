#!/usr/bin/env python3

import os
import sys
from pathlib import Path
import fitz
from pprint import pprint


print("Hello .. Welcome to the Python Stamp Utility")
print("The OS is: ", os.name)
print()
print(sys.argv)


stamp_file=sys.argv[1]
unstamped_files=sys.argv[2]
stamped_folder=sys.argv[3]
zipped_filename=sys.argv[4]
stamped_files_folder_name=sys.argv[5]


stamp_width = 75
stamp_height = 75

distance_from_right  = 165
distance_from_bottom = 105


def get_final_path(path, dir):
    int_path = path.split("/")
    int_path.pop(3)
    int_path[2] = dir
    d_path = "/".join(int_path)

    return d_path


def create_final_paths(files_list):
    for file in files_list:
        dst_path = file[1]
        Path(dst_path).mkdir(parents=True, exist_ok=True)


def get_files_to_stamp(dir):
    file_paths = []

    for path, directories, files in os.walk(dir):
        # print("Path: ", path, "File: ", files)

        for filename in files:
            if filename.endswith(".pdf"):
                tmp_lst = []
                filepath = os.path.join(path, filename)
                tmp_lst.append(filepath)

                final_path = os.path.join(get_final_path(path, stamped_files_folder_name), filename)
                tmp_lst.append(final_path)

                file_paths.append(tmp_lst)
    
    return file_paths


def stamp_files(files_list, stamp):


    print(len(files_list))

    for file in files_list:
        # pprint(file[0])
        src_file = file[0]
        dst_file = file[1]

        doc = fitz.open(src_file)

        if doc.is_pdf:
            for page in doc:
                page_width = page.rect.width
                page_height = page.rect.height
                    
                # print((page_width), type(page_width))
                # print((page_height), type(page_height))

                start_width = (page_width - distance_from_right)
                start_height = (page_height - distance_from_bottom)
                
                end_width = start_width + stamp_width
                end_height = start_height + stamp_height

                coords = fitz.Rect(start_width, start_height, end_width, end_height)
                page.insert_image(coords, filename=stamp)



            doc.ez_save(dst_file)
        

def get_file_info(file):
    file_data = {}

    doc = fitz.open(file)

    file_data["can_save_incrementally"] = doc.can_save_incrementally()
    file_data["toc"] = doc.get_toc()
    file_data["layout"] = doc.layout()
    file_data["is_pdf"] = doc.is_pdf
    file_data["page_count"] = doc.page_count
    file_data["page_layout"] = doc.pagelayout

    return file_data


def get_files_info(files_list):
    for file in files_list:
        src = file[0]
        pprint(get_file_info(src))





b= get_files_to_stamp(unstamped_files)

create_final_paths(b)

get_files_info(b)

stamp_files(b, stamp_file)

