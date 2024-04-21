#!/usr/bin/env python3

import fitz

def get_file_info(file, *arg):
    file_info = {}

    doc = fitz.open(file)

    for a in arg:
        file_info[a] = getattr(doc, a, "Not Available")
    
    return file_info

