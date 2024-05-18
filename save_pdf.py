#!/usr/bin/env python3

import sys
import pdfkit
# import weasyprint

url = sys.argv[1]

pdfkit.from_url(url, 'pdfkit_out.pdf')

# pdf = weasyprint.HTML(url).write_pdf()
# open('weasy_print.pdf', 'wb').write(pdf)


