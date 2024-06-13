#!/usr/bin/env python3



import os
from pathlib import Path


def create_filtered_files(src_dir: str, work_dir: str, dst_dir: str, type_of_file="pdf"):
    filtered_files = {}
    unoperated_files = {}

    for path in Path(src_dir).rglob(f"*.{type_of_file}"):
        tmp_file = {}
        if path.is_file():
            tmp_file["filename"] = os.path.basename(path)
            tmp_file["filepath"] = str(path)
            tmp_file["working_path"] = str(path).replace(str(src_dir), str(work_dir))
            tmp_file["dst_path"] = str(path).replace(str(src_dir), str(dst_dir))
        filtered_files[str(path)] = tmp_file

    print("Total PDF Files: ", len(filtered_files))
    return filtered_files



def files_not_processed(src_dir: str, type_of_file=".pdf"):
    unprocessed_files = []

    for path in Path(src_dir).rglob("*.*"):
        filename, file_ext = os.path.splitext(str(path).lower())
        # tmp_file = {}
        if path.is_file():
            if file_ext != type_of_file:
                unprocessed_files.append(str(path))
    
    return unprocessed_files
        




