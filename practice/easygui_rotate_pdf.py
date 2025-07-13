import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter

file_path = gui.fileopenbox(msg="Select the PDF file", default="*.pdf")
if file_path is None:
    exit()

degree_list = [90, 180, 270]
degree = gui.enterbox(msg="Enter degree for rotation, 90, 180, or 270")
while degree is None or (degree == '') or (int(degree) not in degree_list):
    degree = gui.enterbox(msg="Enter degree for rotation, 90, 180, or 270")

degree = int(degree)
filetype = "*.pdf"
save_file_path = gui.filesavebox(
    msg="Select file to save rotated file", default=filetype
)

if save_file_path is None:
    exit()

while save_file_path == file_path:
    gui.msgbox(msg="rotated file can not be saved in the same file")
    save_file_path = gui.filesavebox(
        msg="Select file to save rotated file", default=filetype
    )

reader = PdfFileReader(file_path)
writer = PdfFileWriter()

for page in reader.pages:
    page.rotateClockwise(degree)
    writer.addPage(page)

with open(save_file_path, mode="wb") as output_file:
    writer.write(output_file)
