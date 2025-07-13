from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

copy_pp_file_path = Path.cwd() / "my_folder" / "PP_copy.pdf"
pp_file_path = Path.cwd() / "my_folder" / "PP.pdf"

pp_reader = PdfFileReader(str(pp_file_path))
copy_pp_file_path_writer = PdfFileWriter()

copy_pp_file_path_writer.appendPagesFromReader(pp_reader)
print(copy_pp_file_path_writer.getNumPages())
with copy_pp_file_path.open(mode="wb") as output_file:
    copy_pp_file_path_writer.write(output_file)
