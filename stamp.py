#!/usr/bin/env python3

import os
import sys
import fitz


print("Hello .. Welcome to the Python Stamp Utility")
print("The OS is: ", os.name)

print(sys.argv)


stamps_folder=sys.argv[1]
unstamped_files=sys.argv[2]
stamped_folder=sys.argv[3]
zipped_filename=sys.argv[4]
stamped_files_folder_name=sys.argv[5]

def get_final_path(path, dir):
    int_path = path.split("/")
    int_path.pop(3)
    int_path[2] = dir
    d_path = "/".join(int_path)

    return d_path


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

b= get_files_to_stamp(unstamped_files)
print(len(b))
print(b)



 



# doc = fitz.open("./data/uns_files/books/book-007.pdf")

# print("Is this file a pdf file: ", doc.is_pdf)
# print("Document Metadata: ", doc.metadata)
# print("Document Name: ", doc.name)
# print("Document No of Pages: ", doc.page_count)
# print("Document Permissions: ", doc.permissions)
# print("Document Page Mode: ", doc.pagemode)
# print("Document Page Layout: ", doc.pagelayout)
# print("Document Needs Password: ", doc.needs_pass)

# doc.close()
