from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import copy


def crop(page):
    left_page = copy.deepcopy(page)
    right_page = copy.deepcopy(page)
    # print(page.mediaBox)
    # get left side of the page
    upper_right = left_page.mediaBox.upperRight
    new_coor = (upper_right[0] / 2, upper_right[1])

    left_page.mediaBox.upperRight = new_coor
    right_page.mediaBox.upperLeft = new_coor

    return left_page, right_page


if __name__ == "__main__":

    last_page_path = Path.cwd() / "PDF" / "last_page.pdf"

    pdf_reader = PdfFileReader(str(last_page_path))
    page = pdf_reader.getPage(0)

    left_page, right_page = crop(page)

    cropped_path = Path.cwd() / "PDF" / "cropped_page.pdf"
    cropped_pdf_writer = PdfFileWriter()
    cropped_pdf_writer.addPage(left_page)
    cropped_pdf_writer.addPage(right_page)

    with cropped_path.open(mode="wb") as file:
        cropped_pdf_writer.write(file)
