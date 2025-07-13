from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

last_page_file_path = Path.cwd() / "my_folder" / "last_page.pdf"
crop_file_path = Path.cwd() / "my_folder" / "crop_last_page.pdf"

pdf_reader = PdfFileReader(str(last_page_file_path))
pdf_writer = PdfFileWriter()

page = pdf_reader.getPage(0)
print(page.mediaBox.lowerLeft)
print(page.mediaBox.lowerRight)
print(page.mediaBox.upperLeft)
print(page.mediaBox.upperRight)

page.mediaBox.upperLeft = (0, 500)

pdf_writer.addPage(page)
with crop_file_path.open(mode="wb") as file:
    pdf_writer.write(file)
