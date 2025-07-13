from pathlib import Path
from PyPDF2 import PdfFileMerger

main_dir = "C:/Users/maste/Documents/Arpit/Scan documents/B.E"

I_sem_a = main_dir + "/BE I Sem A.pdf"
I_sem_b = main_dir + "/BE I Sem B.pdf"
II_sem_a = main_dir + "/BE II Sem A.pdf"
II_sem_b = main_dir + "/BE II Sem B.pdf"
III_sem_a = main_dir + "/BE III Sem A.pdf"
III_sem_b = main_dir + "/BE III Sem B.pdf"
IV_sem_a = main_dir + "/BE IV Sem A.pdf"
IV_sem_b = main_dir + "/BE IV Sem B.pdf"


pdf_merger = PdfFileMerger()
pdf_merger.append(str(I_sem_a))
pdf_merger.append(str(I_sem_b))
pdf_merger.append(str(II_sem_a))
pdf_merger.append(str(II_sem_b))
pdf_merger.append(str(III_sem_a))
pdf_merger.append(str(III_sem_b))
pdf_merger.append(str(IV_sem_a))
pdf_merger.append(str(IV_sem_b))

# pdf_merger.merge(1, str(extract_page_file_path))

with Path(Path.cwd() / "BE.pdf").open(
    mode="wb"
) as output_file:
    pdf_merger.write(output_file)
