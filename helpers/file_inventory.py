#!/usr/bin/env python3

import os
from pathlib import Path

def create_filtered_files(directory, type_of_file="pdf"):
    list_of_files = []

    for path in Path(directory).rglob(f"*.{type_of_file}"):
        if path.is_file():
            list_of_files.append(str(path))
            
    return list_of_files


def create_filtered_src_dst_files(src_dir, dst_dir, type_of_file="pdf"):
    list_of_files = []

    for path in Path(src_dir).rglob(f"*.{type_of_file}"):
        
        if path.is_file():
            tmp_lst = []
            tmp_lst.append(str(path))
            tmp_lst.append(str(path).replace(str(src_dir), str(dst_dir)))
            list_of_files.append(tmp_lst)
            
    return list_of_files


def create_filtered_dst_files(src_dir, dst_dir, type_of_file="pdf"):
    list_of_files = []

    for path in Path(src_dir).rglob(f"*.{type_of_file}"):
        if path.is_file():
            list_of_files.append(str(path).replace(str(src_dir), str(dst_dir)))
            
    return list_of_files


def create_filtered_dst_folder(src_dir, dst_dir, type_of_file="pdf"):
    list_of_folders = []

    for path in Path(src_dir).rglob(f"*.{type_of_file}"):
        if path.is_file():
            dst_file = str(path).replace(str(src_dir), str(dst_dir))
            list_of_folders.append(os.path.split(dst_file)[0])
        
            
    return list_of_folders


def create_filtered_unique_dst_folder(src_dir, dst_dir, type_of_file="pdf"):

    list_of_all_folders = []
    unique_folders = []

    for path in Path(src_dir).rglob(f"*.{type_of_file}"):
        if path.is_file():
            dst_file = str(path).replace(str(src_dir), str(dst_dir))
            list_of_all_folders.append(os.path.split(dst_file)[0])
        
    for item in list_of_all_folders:
        if item not in unique_folders:
            unique_folders.append(item)
        
            
    return unique_folders

