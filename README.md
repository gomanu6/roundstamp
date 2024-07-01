# roundstamp
- Round Stamp It!
- Current Stable version: v0.6a
- rs6.sh


### Fitz use cases
- [How to Make one PDF of all your Pictures (or Files)](https://pymupdf.readthedocs.io/en/latest/recipes-images.html#how-to-make-one-pdf-of-all-your-pictures-or-files)

### Pre requisites
- bash
- python3
- python3-venv
- python3-pip
- [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/)


### Features to add
- Dockerize
- Error Checking and not crashing
- Convert and Stamp Image files (JPG | PNG)
- logging
- send logs by emails
- Accept a Folder or a Zip File
- Files not Processed - returns a list


### Stamp and Overwrite
- start with a zip file
    - does not support formats other than .zip
- unzip in a folder
    - data/unstamped
- Path().rglob()
    - create a filtered dict of files
    - change destination-filename
- create pixmaps
- convert back to pdf
- stamp pdf
- re-create pixmaps
- convert pixmaps into single pdf
- zip into new archive
- delete old archive and folder


### Bash Commants and Utilities used
- stat -c %U
- stat -c %G
- mkdir
    - v = verbose
    - p = create parents
- cp
    - r = recursive
    - v = verbose
- unzip
    - q = quiet
    - o - overwrite
- rm
    - r = recursive
    - f = force
- python3

### Python Libraries used
- os
- sys
- pathlib
- time
- pprint
- pymupdf
    - fitz

### [Fitz Document Class](https://pymupdf.readthedocs.io/en/latest/document.html)
- fitz.Matrix(2,2)

#### [Fitz Document Class Methods (relevant)](https://pymupdf.readthedocs.io/en/latest/document.html)
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

#### Fitz Document Class Attributes (relevant)
- Document.name
- Document.needs_pass
- Document.is_encrypted
- Document.is_pdf
- Document.is_closed
- Document.is_dirty = PDF only: has document been changed yet?
- Document.metadata
- Document.page_count
- Document.pagelayout
- Document.version_count


### [Fitz Page Class Methods and Attributes](https://pymupdf.readthedocs.io/en/latest/page.html)

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
    - Page.rect.width
    - Page.rect.height
- Page.rotation

### [Fitz Pixmap](https://pymupdf.readthedocs.io/en/latest/pixmap.html)

- Pixmap.save()
- Pixmap.pil_save()
- Pixmap.set_dpi()
- Pixmap.convert_to_pdf()
- Pixmap.alpha
- Pixmap.width
- Pixmap.height


### References
- [Virtual Environments](https://ioflood.com/blog/python-activate-venv/)
- [How to Run a Python CLI Tool Inside a Docker Container](https://dteslya.engineer/blog/2022/07/14/how-to-run-a-python-cli-tool-inside-a-docker-container/)
- [Dockerize Your Python Command-Line Program](https://medium.com/swlh/dockerize-your-python-command-line-program-6a273f5c5544)