from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

PP_path = Path.cwd() / "PDF" / "PP.pdf"
rotate_path = Path.cwd() / "PDF" / "rotated.pdf"

pdf_reader = PdfFileReader(str(PP_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    page.rotateCounterClockwise(90)
    pdf_writer.addPage(page)

with rotate_path.open(mode="wb") as file:
    pdf_writer.write(file)
