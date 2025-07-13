from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

PP_file_path = Path.cwd() / "my_folder" / "PP.pdf"

part_1_file_path = Path.cwd() / "my_folder" / "part_1.pdf"

part_2_file_path = Path.cwd() / "my_folder" / "part_2.pdf"

# define filereader and filewriter
pp_reader = PdfFileReader(str(PP_file_path))
part_1_writer = PdfFileWriter()
part_2_writer = PdfFileWriter()

# get total number of pages
total_number_of_pages = pp_reader.getNumPages()

# get first 150 pages and write them in part_1 writer object
for page in pp_reader.pages[:150]:
    part_1_writer.addPage(page)

# get remaining number of pages and write them in part_2 writer object
for page in pp_reader.pages[150:]:
    part_2_writer.addPage(page)

# write the part_1 and part_2 writer object data in the respective files
with part_1_file_path.open(mode="wb") as output_file:
    part_1_writer.write(output_file)

with part_2_file_path.open(mode="wb") as output_file:
    part_2_writer.write(output_file)
