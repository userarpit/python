import img2pdf
from PIL import Image


def convert_jpg_to_pdf(jpg_path, pdf_path):
    """
    Converts a JPG image to a PDF file.

    Args:
        jpg_path (str): The path to the input JPG image.
        pdf_path (str): The path to save the output PDF file.
    """
    try:
        img = Image.open(jpg_path)
        with open(pdf_path, "wb") as f:
            f.write(img2pdf.convert(img.filename))
        print(f"Successfully converted '{jpg_path}' to '{pdf_path}'")
    except FileNotFoundError:
        print(f"Error: JPG file not found at '{jpg_path}'")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    jpg_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\13.jpg"  # Replace with your JPG file path
    pdf_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\13.pdf"  # Replace with your desired PDF file path
    convert_jpg_to_pdf(jpg_file, pdf_file)

    jpg_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\14.jpg"  # Replace with your JPG file path
    pdf_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\14.pdf"  # Replace with your desired PDF file path
    convert_jpg_to_pdf(jpg_file, pdf_file)

    jpg_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\15.jpg"  # Replace with your JPG file path
    pdf_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\15.pdf"  # Replace with your desired PDF file path
    convert_jpg_to_pdf(jpg_file, pdf_file)

    jpg_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\16.jpg"  # Replace with your JPG file path
    pdf_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\16.pdf"  # Replace with your desired PDF file path
    convert_jpg_to_pdf(jpg_file, pdf_file)

    jpg_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\17.jpg"  # Replace with your JPG file path
    pdf_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\17.pdf"  # Replace with your desired PDF file path
    convert_jpg_to_pdf(jpg_file, pdf_file)

    jpg_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\18.jpg"  # Replace with your JPG file path
    pdf_file = "C:\\Users\\maste\\Documents\\Arpit\\print\\18.pdf"  # Replace with your desired PDF file path
    convert_jpg_to_pdf(jpg_file, pdf_file)
    