from PyPDF2 import PdfMerger
import os


def merge_pdfs(pdf_paths, output_path):
    """
    Merges multiple PDF files into a single PDF.

    Args:
        pdf_paths (list): List of paths to the PDF files to merge.
        output_path (str): Path to save the merged PDF.
    """
    merger = PdfMerger()
    for pdf_path in pdf_paths:
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as pdf_file:
                merger.append(pdf_file)
        else:
            print(f"Warning: File not found: {pdf_path}")
    merger.write(output_path)
    merger.close()


if __name__ == "__main__":
    pdf_files = [
        "C:\\Users\\maste\\Documents\\Arpit\\print\\1.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\2.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\3.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\4.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\5.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\6.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\7.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\8.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\9.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\10.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\11.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\12.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\13.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\14.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\15.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\16.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\17.pdf",
        "C:\\Users\\maste\\Documents\\Arpit\\print\\18.pdf",
    ]  # Replace with your PDF file paths

    output_pdf = "merged_file.pdf"
    merge_pdfs(pdf_files, output_pdf)
    print(f"Merged PDF saved to {output_pdf}")
