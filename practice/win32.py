from win32com import client as wc
w = wc.Dispatch("Word.Application")
doc = w.Documents.Open("file_name.doc")
doc.SaveAs("file_name.docx", 16)
# doc.close()