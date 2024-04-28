#!/usr/bin/env python3

import os
from pathlib import Path
import fitz
from helpers.dpprint import dpprint
import helpers.file_inventory as fi




def create_pixmaps(list, src_dir, dst_dir, stamp_file):
    
    final_list = fi.create_filtered_src_dst_files(src_dir, dst_dir)

    list_of_pixmaps = []

    for file in final_list:
        src_file = file[0]
        dst_file = file[1]
        list_of_pixmaps.append(dst_file)
        # print("Processing ", src_file)
        Path(dst_file).mkdir(parents=True, exist_ok=True)

        doc = fitz.open(src_file)
        matrix = fitz.Matrix(1, 1)    

        # filename = doc.name
        # img_p = os.path.join(dst_file, filename)
        # print("Creating Folder -->>", dst_file)
        # print("Basename--->>", os.path.basename(dst_file))

        for page in doc:
            pix = page.get_pixmap(matrix=matrix)
            img_filename = "page-%06i.png" % (page.number)
            img_path = os.path.join(dst_file, img_filename)
            pix.save(img_path)
    

        
        # img_list = os.listdir(dst_file)
        # img_list.sort()
        # # dpprint(img_list)




        # new_doc = fitz.open()

        # for i, f in enumerate(img_list):
        #     print("i is -->", i)
        #     print("f is -->", f)
        #     # print("Source File is -->>", src_file)
        #     image_path = os.path.join(dst_file, f)
        #     print(image_path)
        #     img = fitz.open(image_path)
        #     rect = img[0].rect
        #     pdfbytes = img.convert_to_pdf()
        #     img.close()

        #     imgpdf = fitz.open("pdf", pdfbytes)
        #     page = new_doc.new_page( width = rect.width, height = rect.height)
        #     page.show_pdf_page(rect, imgpdf, 0)
        #     savepath = os.path.join(dst_file, os.path.basename(dst_file))
        # new_doc.ez_save(dst_file)

        
        
        
        
        
        # for img in os.listdir(dst_file):
        #     print(dst_file, img)
        #     imgpath = os.path.join(dst_file, img)
        #     print(imgpath)
        #     # st_pg = img.split(".")[0]
        #     # st_pagename = "st_%s.pdf" % (st_pg)
        #     imgfile = fitz.open(imgpath)
        #     rect = imgfile[0].rect
        #     pdfbytes = imgfile.convert_to_pdf()
        #     imgfile.close

        #     imgpdf = fitz.open("pdf", pdfbytes)

        #     page = new_doc.new_page(width = rect.width, height = rect.height)
        #     page.show_pdf_page(rect, imgpdf, 0)
        # new_doc.ez_save()



            # print(type(doc))
            # page = doc[0]
            # print(type(page))
            # start_width = page.rect.width - 100
            # start_height = page.rect.height - 100
            # coords = fitz.Rect(start_width, start_height, start_width + 75, start_height + 75)
            # page.insert_image(coords, filename=stamp_file)
            # save_path = os.path.join(dst_file, st_pagename)
            # doc.ez_save(save_path)
            # pix = fitz.Pixmap(img)
            # imgpdf = fitz.open("pdf", pix.pdfocr_tobytes())
            # doc.insert_pdf(imgpdf)
            # pix = None
            # imgpdf.close()
            
        
        doc.close()

    return list_of_pixmaps









