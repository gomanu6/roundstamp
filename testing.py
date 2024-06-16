#!/usr/bin/env python3

import os
# import sys
from pathlib import Path
# import fitz
from pprint import pprint


# from helpers import add_numbers as am


# stamp_file=sys.argv[1]
# unstamped_folder=sys.argv[2]
# stamped_folder=sys.argv[3]
# images_folder=sys.argv[4]
# zipped_filename=sys.argv[4]

fol="/mnt/mounts/bansrv001/books"


# tree = os.walk(fol)

# pprint(list(tree))

document_types = [ "*.doc", "*.docx", "*.txt"]
doc_files = []

for type in document_types:
     for path in Path(fol).rglob(f"{type}"):
          doc_files.append(str(path))

pprint(doc_files)



# walked = os.walk(fol, topdown=True)
# all_files = {
#         "all_pdf_files": {},
#         "document_files": {},
#         "unprocessed_files": []
# }
# for (root, dirs, files) in walked:
#         # print (root)
#         # print (dirs)
#         # print (files)
#         # print ('--------------------------------')
#         for file in files:
#                 # print(file)
#                 file_path = os.path.join(root, file)
#                 filename = file
#                 destination_path = file_path.replace("mounts", "destination")
#                 working_path = file_path.replace("mounts", "working")
                
#                 tmp_file = {}
#                 if file.lower().endswith(".pdf"):
#                         tmp_file["filename"] = filename
#                         tmp_file["filepath"] = file_path
#                         tmp_file["dst_path"] = destination_path
#                         tmp_file["working_path"] = working_path
#                         all_files["all_pdf_files"][file_path] = tmp_file
#                 else:
#                         all_files["unprocessed_files"].append(file_path)


#         # print("***")




# pprint(all_files)
# pprint(all_files["all_pdf_files"].keys())
# for key in all_files["all_pdf_files"].keys():
#         pprint(key)
# print("**********")
# for key in all_files["unprocessed_files"]:
#         pprint(key)