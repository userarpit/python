from PyPDF2 import PdfFileWriter
from pathlib import Path

pdf_path = Path.cwd() / "my_folder" / "blank.pdf"

pdf = PdfFileWriter()
pdf.addBlankPage(width=72, height=72)

with pdf_path.open(mode="wb") as output_file:
    pdf.write(output_file)
