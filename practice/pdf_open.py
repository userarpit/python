from pathlib import Path
from PyPDF2 import PdfFileReader

file_path = Path.cwd() / "my_folder" / "PP.txt"
pdf_path = Path.cwd() / "my_folder" / "PP.pdf"

pdf = PdfFileReader(str(pdf_path))

with file_path.open(mode="w", encoding="utf-16") as file:
    title = pdf.documentInfo.title
    num_of_pages = pdf.getNumPages()
    file.write(f"{title}\nNumber of Pages:{num_of_pages}\n\n")

    for page in pdf.pages:
        text = page.extractText()
        file.write(text)
