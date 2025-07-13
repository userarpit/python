from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

last_page_file_path = (
    Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")
    / "last_page_rotate.pdf"
)

pdf_reader = PdfFileReader(str(last_page_file_path))
pdf_writer = PdfFileWriter()

page = pdf_reader.pages[0]
if page["/Rotate"] % 360 == 180:
    page.rotateClockwise(180)
pdf_writer.addPage(page)
# print(page['/Rotate'])

last_page_rotate_file_path = Path.cwd() / "my_folder" / "last_page_rotate.pdf"
with last_page_rotate_file_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
