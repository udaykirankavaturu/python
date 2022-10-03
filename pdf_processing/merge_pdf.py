import sys
import PyPDF2
import sys

pdfs = sys.argv[1:]


def pdf_merger(pdfs):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write('merged.pdf')


pdf_merger(pdfs)
