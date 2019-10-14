from PyPDF2 import PdfFileReader, PdfFileWriter


input_pdf = PdfFileReader('files/The Emperor.pdf') # read input pdf with Reader
output_pdf = PdfFileWriter() # initialize pdf writer

cover = PdfFileReader('files/Emperor cover sheet.pdf') # read pdf with cover
cover = cover.getPage(0) # extract page from pdf with cover
output_pdf.addPage(cover) # add cover to writer object
for page in input_pdf.pages:
    output_pdf.addPage(page) #add pages from Emperor.pdf to writer object 

with open('files/Covered Emperor.pdf', 'wb') as file: # create a pdf-file with write binary mode
    output_pdf.write(file) # write pdf writer object with contents to file
