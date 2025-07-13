from pathlib import Path

from PyPDF2 import PdfFileReader, PdfFileWriter

PP_file_path = (
    Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder") / "PP.pdf"
)

every_other_page_file_path = (
    Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")
    / "every_other_page.pdf"
)

# define reader and writer
PP_reader = PdfFileReader(str(PP_file_path))
every_other_page_writer = PdfFileWriter()

# get total number of pages
total_number_of_pages = PP_reader.getNumPages()

# get the even number page, and add in the writer object
for page in PP_reader.pages[::2]:
    every_other_page_writer.addPage(page)

# open the every_other_page file and the write the pages
with every_other_page_file_path.open(mode="wb") as output_file:
    every_other_page_writer.write(output_file)
