# roundstamp
Round Stamp It!

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
- stat -c %U,
- stat -c %G
- mkdir
- cp
- unzip
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

- Page.get_pixmap()
- Page.insert_image()
- Page.get_text()
- Page.insert_text()
- Page.search_for()


- Page.number
- Page.rect
- Page.rotation



### References
- [Virtual Environments](https://ioflood.com/blog/python-activate-venv/)