from pathlib import Path
from PyPDF2 import PdfFileMerger

main_dir = Path(r"C:\Users\maste\Documents\Arpit\Python\practice\my_folder")

all_3_report = list(main_dir.glob("*_page.pdf"))
all_3_report.sort()


pdf_merger = PdfFileMerger()
for path in all_3_report:
    pdf_merger.append(str(path))

with Path(Path.cwd() / ("my_folder/all_3_report_pages.pdf")).open(
    mode="wb"
) as output_file:
    pdf_merger.write(output_file)
