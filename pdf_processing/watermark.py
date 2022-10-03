import PyPDF2

input_file = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
watermark_file = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
writer = PyPDF2.PdfFileWriter()

for page_number in range(input_file.getNumPages()):
    page = input_file.getPage(page_number)
    page.mergePage(watermark_file.getPage(0))
    writer.addPage(page)
    with open('watermarked_file.pdf', 'wb') as new_file:
        writer.write(new_file)
