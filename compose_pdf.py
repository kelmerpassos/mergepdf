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
    file_info = open('files_composer.txt', 'r')
    i = 0
    name = '' 
    path = '' 
    pdf_files = []
    for f in file_info:
        i+=1
        if i == 1:
            path = rm_next(f)
        elif i == 2:
            name = rm_next(f)
        elif rm_next(f).endswith(".pdf"):
            pdf_files.append(rm_next(f))
    file_info.close()
    merger = PdfFileMerger()
    for filename in pdf_files:
        print('Adicionando: ', filename)
        merger.append(PdfFileReader(filename), "rb")
    print('Criando aqrquivo: ', os.path.join(path, name))
    merger.write(os.path.join(path, name))
    for filename in pdf_files:
        print('Excuindo: ', filename)
        os.remove(filename)
