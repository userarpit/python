from PyPDF2 import PdfFileReader, PdfFileWriter
import easygui as gui

filetype = "*.pdf"
file_path = gui.fileopenbox(msg="Select file ", default="*.pdf")
if file_path is None:
    exit()

reader = PdfFileReader(file_path)
writer = PdfFileWriter()

start_page = gui.enterbox(msg="Enter starting page")

while True:
    if start_page is None:
        exit()
    elif not start_page.isdigit() or start_page == "0" or int(start_page) <= 0:
        gui.msgbox(msg="Entry is invalid!")
        start_page = gui.enterbox(msg="Enter starting page number")
    else:
        break

start_page = int(start_page)

end_page = gui.enterbox(msg="Enter ending page number")
# print(end_page)
while True:
    if end_page is None:
        exit()
    elif not end_page.isdigit() or end_page == "0" or int(end_page) <= 0:
        gui.msgbox(msg="Entry is invalid!")
        end_page = gui.enterbox(msg="Enter ending page number")
    elif int(end_page) < start_page:
        gui.msgbox(msg="End page must be greater than start page number")
        end_page = gui.enterbox(msg="Enter ending page number")
    else:
        break

end_page = int(end_page)

save_file_path = gui.filesavebox(msg="Enter save file location", default=filetype)
if save_file_path is None:
    exit()

while save_file_path == file_path:
    gui.msgbox(msg="can not override original file")
    save_file_path = gui.filesavebox(
        msg="Enter save file locatio", default=filetype
    )

for page in reader.pages[start_page-1:end_page]:
    writer.addPage(page)

with open(save_file_path, mode="wb") as output_file:
    writer.write(output_file)
