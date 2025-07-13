from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import crop_left_right_half

rotated_path = Path.cwd() / "PDF" / "PP.pdf"
split_path = Path.cwd() / "PDF" / "split.pdf"

pdf_reader = PdfFileReader(str(rotated_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    # print(page.mediaBox.upperRight)
    left_page, right_page = crop_left_right_half.crop(page)
    pdf_writer.addPage(left_page)
    pdf_writer.addPage(right_page)

with split_path.open(mode="wb") as file:
    pdf_writer.write(file)
