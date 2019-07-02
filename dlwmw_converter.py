import os
import win32com
from win32com import client as wc
path='C:\\Users\\Peter\\Desktop\\dlwmw-test\\'
path_docx='C:\\Users\\Peter\\Desktop\\dlwmw-docx\\'
doclist=os.listdir(path)
word=wc.Dispatch('Word.Application')
for name in doclist:
    doc=word.Documents.Open(path+name)
    name_docx=name+'x'
    doc.SaveAs(path_docx+name_docx,12)
    print(name_docx)
    doc.Close()
word.Quit()
print('convert completed')
