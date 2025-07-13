from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

seven_page = (
    Path(r"C:\Users\maste\Documents\Arpit\Scan documents\B.E")
    / "BE.pdf"
)

pdf_reader = PdfFileReader(str(seven_page))
pdf_writer = PdfFileWriter()

for i, page in enumerate(pdf_reader.pages):
    if i == 6:
        page.rotateCounterClockwise(90)
        
    pdf_writer.addPage(page)

print(page["/Rotate"])
final_BE = Path(r"C:\Users\maste\Documents\Arpit\Scan documents\B.E") / "Final_BE.pdf"
with final_BE.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
