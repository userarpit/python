from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pp_file_path = Path.cwd() / "my_folder" / "PP.pdf"
last_page_file_path = Path.cwd() / "my_folder" / "last_page.pdf"

pp_file_reader = PdfFileReader(str(pp_file_path))
# print(pp_file_reader.getNumPages())

last_page_writer = PdfFileWriter()
last_page = pp_file_reader.pages[-1]
last_page_writer.addPage(last_page)

with last_page_file_path.open(mode="wb") as output_file:
    last_page_writer.write(output_file)
