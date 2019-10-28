import copy
from PyPDF2 import PdfFileReader, PdfFileWriter


walrus_pdf = PdfFileReader('files\Walrus.pdf')
output_pdf = PdfFileWriter()
walrus_pdf.decrypt('IamtheWalrus')
for page in range(0, walrus_pdf.getNumPages()):
    page = walrus_pdf.getPage(page)
    page.rotateClockwise(270)
    page_right = copy.copy(page)
    upper_right = page.mediaBox.upperRight
    new_coords = (upper_right[0] / 2, upper_right[1])
    page.mediaBox.upperRight = new_coords
    output_pdf.addPage(page)
    page_right.mediaBox.upperLeft = new_coords
    output_pdf.addPage(page_right)

with open('files\Walrus_Rotate.pdf', 'wb') as output_file:
    output_pdf.write(output_file)
