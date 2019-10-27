from PyPDF2 import PdfFileReader, PdfFileWriter

path = 'files\The Whistling Gypsy.pdf'
pdf_file = PdfFileReader(path)
output_pdf = PdfFileWriter()
doc_info = pdf_file.getDocumentInfo()
print(f'TITLE: {doc_info.title}')
print(f'AUTHOR: {doc_info.author}')
print(f'Number of pages: {pdf_file.getNumPages()}')
page1 = pdf_file.getPage(1)
output_pdf.addPage(page1)
song = page1.extractText().encode('utf-8')

with open('files\The Whistling Gypsy Song.txt', 'wb') as output:
    output.write(song)
    
with open('files\The Whistling Gypsy (No cover).pdf', 'wb') as output_file:
    output_pdf.write(output_file)
