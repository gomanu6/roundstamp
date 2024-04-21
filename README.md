# roundstamp
Round Stamp It!


### Fitz use cases
- [How to Make one PDF of all your Pictures (or Files)](https://pymupdf.readthedocs.io/en/latest/recipes-images.html#how-to-make-one-pdf-of-all-your-pictures-or-files)

### Pre requisites
- bash
- python3
- python3-venv
- python3-pip
- [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/)


### Stamp and Overwrite
- start with a zip file
    - does not support formats other than .zip

- unzip in a folder
- modify and overwrite
- change destination-filename
- zip into new archive
- delete old archive and folder

### Commants and Utilities used
- stat -c %U
- stat -c %G
- mkdir
    - v = verbose
    - p = create parents
- cp
    - r = recirsive
    - v = verbose
- unzip
    - q = quiet
    - o - overwrite
- python3

### Python Libraries used
- os
- pymupdf
    - fitz

### Fitz Document Class

#### Fitz Document Class Methods (relevant)
- Document.ez_save()
- Document.save()
- Document.saveIncr()
- Document.close()
- Document.can_save_incrementally()
- Document.convert_to_pdf()
- Document.copy_page()
- Document.delete_page()
- Document.delete_pages()
- Document.fullcopy_page()
- Document.get_page_pixmap()
- Document.get_toc()
- Document.insert_page()
- Document.insert_pdf()
- Document.insert_file()
    - infile (multiple) – the input document to insert. May be a filename specification as is valid for creating a Document or a Pixmap.
- Document.layout()
- Document.load_page()
- Document.move_page()
- Document.new_page()
- Document.pages()
- Document.search_page_for()

#### Fitz DOcument Class Attributes (relevant)
- Document.is_closed
- Document.is_pdf
- Document.metadata
- Document.name
- Document.page_count
- Document.pagelayout


### Fitz Page Class Methods and Attributes~

- Page.get_pixmap(matrix=matrix)
- Page.insert_image()
    - 
- Page.show_pdf_page()
    - show_pdf_page(rect, docsrc, pno=0, keep_proportion=True, overlay=True, oc=0, rotate=0, clip=None)
    - 
- Page.get_text()
- Page.insert_text()
- Page.search_for()


- Page.number
- Page.rect
- Page.rotation

### Fitz Pixmap

- Pixmap.save()
- Pixmap.pil_save()
- Pixmap.set_dpi()
- Pixmap.alpha
- Pixmap.width
- Pixmap.height
- 


### References
- [Virtual Environments](https://ioflood.com/blog/python-activate-venv/)