#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint



def create_pdf_from_images(list):

    for file in list:
        src_file = file[0]
        dst_file = file[1]
        print(dst_file)

        # list_of_images = os.listdir(dst_file)
        # print("Creating pdf for ", dst_file)
        # dpprint(list_of_images)




