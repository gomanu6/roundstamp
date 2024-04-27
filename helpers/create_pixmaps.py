#!/usr/bin/env python3

import os
from pathlib import Path
import fitz



def create_pixmaps(list, src_dir, dst_dir):
    final_list = []

    for item in list:
        tmp_list = []
        tmp_list.append(item)
        tmp_list.append(str(item).replace(str(src_dir), str(dst_dir)))
        final_list.append(tmp_list)

    for file in final_list:
        src_file = file[0]
        dst_file = file[1]

        doc = fitz.open(src_file)
        matrix = fitz.Matrix(1, 1)    

        # filename = doc.name
        # img_p = os.path.join(dst_file, filename)
        Path(dst_file).mkdir(parents=True, exist_ok=True)

        for page in doc:
            pix = page.get_pixmap(matrix=matrix)
            img_filename = "page-%06i.png" % (page.number)
            img_path = os.path.join(dst_file, img_filename)
            pix.save(img_path)
        
        for img in os.listdir(dst_file):
            print(dst_file, img)
            # pix = fitz.Pixmap(img)
            # imgpdf = fitz.open("pdf", pix.pdfocr_tobytes())
            # doc.insert_pdf(imgpdf)
            # pix = None
            # imgpdf.close()
            
        
        doc.close()









