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
stamped_folder_name=sys.argv[7]

print("Stamp File is: -->>", stamp_file)
print("Unstamped Files Folder: -->>", unstamped_files)
print("Stamped Files Folder:   -->>", stamped_folder)
# print(zipped_filename)
# print(stamped_files_folder_name)
# print(path_to_replace)

import pathlib

stamp_width = 75
stamp_height = 75

distance_from_right  = 165
distance_from_bottom = 105


def list_files_recursively(directory):
    list_of_files = []

    for path in pathlib.Path(directory).rglob('*.pdf'):
        
        if path.is_file():
            tmp_lst = []
            tmp_lst.append(str(path))
            tmp_lst.append(str(path).replace(str(unstamped_files), str(stamped_folder)))

            list_of_files.append(tmp_lst)
            
    return list_of_files


def create_final_paths(files_list):
    print("Creating Final Paths")
    for file in files_list:
        dst_path = file[1]
        Path(dst_path).mkdir(parents=True, exist_ok=True)


def get_file_info(file):
    print()
    print("Getting information for File...")
    file_data = {}

    doc = fitz.open(file)
    print("File Name: ", doc.name)
    file_data["is_pdf"] = doc.is_pdf
    file_data["page_count"] = doc.page_count
    file_data["toc"] = doc.get_toc()
    # file_data[""]
    file_data["can_save_incrementally"] = doc.can_save_incrementally()
    # file_data["layout"] = doc.layout()
    file_data["page_layout"] = doc.pagelayout

    return file_data


def get_files_info(files_list):
    for file in files_list:
        src = file[0]
        pprint(get_file_info(src))


def stamp_files(files_list, stamp):

    print("No of Files to stamp:", len(files_list))
    print("Stamping Files...")

    for file in files_list:
        # pprint(file[0])
        src_file = file[0]
        dst_file = file[1]

        doc = fitz.open(src_file)
        print("Stamping file: -->> ", src_file)
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
            print("Finished Stamping file: -->> ", src_file)


def get_file_pixmap(src_file, dst_file):
    print("Getting pixmap for: --> ", src_file)
    doc = fitz.open(src_file)
    doc.get_page_pixmap(0)
    doc.save(dst_file)


def get_files_pixmap(files_list):
    for file in files_list:
        src = file[0]
        dst = file[1]
        get_file_pixmap(src, dst)



a = list_files_recursively(unstamped_files)
create_final_paths(a)
# get_files_info(a)
# stamp_files(a, stamp_file)

get_files_pixmap(a)




