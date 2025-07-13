from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

path = Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")
pp_file_path = path / "PP.pdf"
first_page_file_path = path / "extract_page.pdf"
copy_pp = path / "PP_copy.pdf"

input_pdf = PdfFileReader(str(pp_file_path))

# get first page - page object

# first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()

for page in input_pdf.pages[0:3]:
    pdf_writer.addPage(page)

with first_page_file_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)
