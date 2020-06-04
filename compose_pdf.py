import os
from PyPDF2 import PdfFileReader, PdfFileMerger

def rm_next(text):
    if text[-1:] == '\n':
        return text[:-1]
    else:
        if text[-2:] == '\\\n':
            return text[:-2]
        else:
            return text


if __name__ == '__main__':    
    file_info = open('files_composer.txt', 'a')
    pdf_files = [rm_next(f) for f in file_info if rm_next(f).endswith(".pdf")]
    merger = PdfFileMerger()

    for filename in pdf_files:
        merger.append(PdfFileReader(os.path.join(rm_next(file_info[0]), filename), "rb"))

    merger.write(os.path.join(rm_next(file_info[0]), rm_next(file_info[1])))