from pathlib import Path
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import blue, red


canvas = Canvas("reyansh.pdf", pagesize=LETTER)

canvas.drawString(1 * inch, 1 * inch, "Reyansh")
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 2 * inch, "Times-Roman 2 inch from bottom")
canvas.drawString(1 * inch, 3 * inch, "Times-Roman 3 inch from bottom")
canvas.drawString(1 * inch, 4 * inch, "Times-Roman 4 inch from bottom")
canvas.drawString(1 * inch, 5 * inch, "Times-Roman 5 inch from bottom")
canvas.drawString(1 * inch, 6 * inch, "Times-Roman 6 inch from bottom")
canvas.setFillColor(red)
canvas.drawString(1 * inch, 7 * inch, "Times-Roman 7 inch from bottom")
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 8 * inch, "Times-Roman 8 inch from bottom")
canvas.setFont("Courier-BoldOblique", 18)
canvas.drawString(1 * inch, 9 * inch, "Times-Roman 9 inch from bottom")
canvas.setFont("Courier-Oblique", 18)
canvas.drawString(1 * inch, 10 * inch, "Times-Roman 10 inch from bottom")
canvas.drawString(1 * inch, 11 * inch, "Times-Roman 11 inch from bottom")

canvas.save()
# canvas1.save()
