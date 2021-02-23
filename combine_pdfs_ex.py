import PyPDF2
from os import listdir
from os.path import isfile, join

'''
Examples:
    * To open PDF *
    f = open('Title', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(f)

    * Get Length *
    pdf_reader.numPages

    * Grab a Page Number *
    page_one = pdf_reader.getPage(0)

    * Get text of a page *
    page_one_text = page_one.extractText()
'''

def combine_pdf(file_path):
    path_name = file_path
    filenames = [f for f in listdir(path_name) if isfile(join(path_name, f))]

    merger = PyPDF2.PdfFileMerger()
    for filename in filenames:
        if filename.endswith('.pdf'):
            print(filename)
            f = open(join(path_name, filename), 'rb')
            merger.append(PyPDF2.PdfFileReader(f))

    merger.write(join(path_name, f"{file_path}.pdf"))

combine_pdf(file_path = 'exam1')