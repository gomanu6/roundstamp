#!/usr/bin/env python3

from pathlib import Path

def create_filtered_files_list(directory, type_of_file="pdf"):
    list_of_files = []

    for path in Path(directory).rglob(f"*.{type_of_file}"):
        
        if path.is_file():
            # tmp_lst = []
            # tmp_lst.append(str(path))
            list_of_files.append(str(path))
            
    return list_of_files


