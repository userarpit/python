from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

PP_path = Path.cwd() / "PDF" / "PP.pdf"
encrypted_path = Path.cwd() / "PDF" / "encrypt.pdf"

pdf_reader = PdfFileReader(str(PP_path))
pdf_writer = PdfFileWriter()

pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_pwd="SuperSecret", owner_pwd="Abcd")

with encrypted_path.open(mode="wb") as file:
    pdf_writer.write(file)

pdf_reader = PdfFileReader(str(encrypted_path))
pdf_reader.decrypt(password="SuperSecret")
page = pdf_reader.getPage(0)
print(page.extractText())