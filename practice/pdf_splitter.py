from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


class PdfFileSplitter:

    def __init__(self, file_name):
        # self.file_name = file_name
        self.file_name_reader = PdfFileReader(str(Path.cwd() / "my_folder" / file_name))

    def split(self, breakpoint):
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()

        for page in self.file_name_reader.pages[:breakpoint]:
            self.writer1.addPage(page)

        for page in self.file_name_reader.pages[breakpoint:]:
            self.writer2.addPage(page)

    def write(self, file_name):
        # create file objects for 2 files - with _1 and _2
        file_name_1 = Path.cwd() / "my_folder" / (file_name + "_1.pdf")
        file_name_2 = Path.cwd() / "my_folder" / (file_name + "_2.pdf")

        with file_name_1.open(mode="wb") as part_1:
            self.writer1.write(part_1)

        with file_name_2.open(mode="wb") as part_2:
            self.writer2.write(part_2)


pdf_splitter = PdfFileSplitter("PP.pdf")

pdf_splitter.split(breakpoint=100)
pdf_splitter.write("PP_split")
