#!/usr/bin/env python3



import os
from pathlib import Path
from pprint import pprint

import fitz


def pass_needed(file):
    doc = fitz.open(file)
    return doc.needs_pass

def no_pages(file):
    doc = fitz.open(file)
    return int(doc.page_count)

def encrypted_doc(file):
    doc = fitz.open(file)
    return doc.is_encrypted


def create_filtered_files(src_dir: str, work_dir: str, dst_dir: str, type_of_file: str ="pdf"):
    filtered_files = {}
    protected_files = []
    unoperated_files = []
    total_pages = 0

    for path in Path(src_dir).rglob(f"*.{type_of_file}"):
        tmp_file = {}
        if path.is_file():
            tmp_file["filename"] = os.path.basename(path)
            tmp_file["filepath"] = str(path)
            tmp_file["working_path"] = str(path).replace(str(src_dir), str(work_dir))
            tmp_file["dst_path"] = str(path).replace(str(src_dir), str(dst_dir))
            tmp_file["no_pages"] = no_pages(str(path))
            tmp_file["needs_pass"] = pass_needed(str(path))
            tmp_file["encrypted"] = encrypted_doc(str(path))
            total_pages += no_pages(str(path))
        filtered_files[str(path)] = tmp_file


    if len(protected_files) > 0:
        print("----Protected Files----")
        for index, file in enumerate(protected_files):
            print(int(index + 1), "--", file)
        print("----End of Protected Files----")
        print()
    else:
        print("--- There were No protected Files found ---")
        print()



    print("Total PDF Files: ", len(filtered_files))
    print("Total Pages: ", total_pages)

    return filtered_files, protected_files



def files_not_processed(src_dir: str, type_of_file: str =".pdf"):
    unprocessed_files = []

    for path in Path(src_dir).rglob("*.*"):
        filename, file_ext = os.path.splitext(str(path).lower())
        # tmp_file = {}
        if path.is_file():
            if file_ext != type_of_file:
                unprocessed_files.append(str(path))
    print("No of Files Not Processed: ", len(unprocessed_files))
    print("---Below Files not Processed---")
    for index, file in enumerate(unprocessed_files):
        print(int(index +1), "--", file)
    print("--- End of Files not Processed ---")

    return unprocessed_files
        

def analyse_files(all_files):
    files = {
        "protected" : []
    }

    for key in all_files.keys():
        tmp = []
        doc = fitz.open(key)
        if doc.needs_pass:
            tmp.append(key)
        files["protected"] += tmp
        
    return files


