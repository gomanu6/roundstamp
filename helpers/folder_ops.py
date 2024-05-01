#!/usr/bin/env python3

import os
from pathlib import Path
import fitz


def create_folder(folder, verbose=False):
    Path(folder).mkdir(parents=True, exist_ok=True)
    if verbose == True:
        print(f"Created Folder {folder}")


def create_folders_from_list(list, verbose=False):
    if verbose == True:
        for folder in list:
            create_folder(folder, verbose=True)
    else:
        for folder in list:
            create_folder(folder)


def get_list_of_unique_folders(list):
    list_of_unique_folders = []

    for item in list:
        folder = os.path.dirname(item)
        if folder not in list_of_unique_folders:
            list_of_unique_folders.append(folder)
        
    return list_of_unique_folders

# def create_folders_for_pixmap(list):
    
#     for file in list:
#         Path(file).mkdir(parents=True, exist_ok=True)

