# This Python file uses the following encoding: utf-8
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.colors import blue, red
import flower

def set_background_color(canvas, color):
    canvas.saveState()
    canvas.setFillColor(color)
    canvas.rect(0, 0, LETTER[0], LETTER[1], fill=1)
    canvas.restoreState()

c = Canvas("Reyansh_Birthday.pdf", pagesize=(5 * inch, 5 * inch))
bg_color = HexColor(0x800080)
set_background_color(c, bg_color)

image_path = str(r"C:\Users\maste\Documents\background.jpeg")
# c.drawImage(image_path, 0, 0, width=LETTER[0], height=LETTER[1])
c.drawImage(r"C:\Users\maste\Documents\reyansh_image.jpg", 1.6 * inch, 2.5 * inch)

c.setFont("Courier-Bold", 15)
c.drawString(1.2 * inch, 2.2 * inch, "Join Us to Celebrate")
c.setFont("Courier-Bold", 20)
c.drawString(1.7 * inch, 1.8 * inch, "Reyansh's")
c.setFont("Courier-Bold", 20)
c.drawString(1.4 * inch, 1.45 * inch, "9th BIRTHDAY")

c.setFont("Courier-Bold", 10)
c.drawString(1.10 * inch, 1.15 * inch, "WEDNESDAY | MARCH 26 | 6PM-8PM")

c.setFont("Courier-BoldOblique", 10)
c.drawString(1.05 * inch, .85 * inch, "225 La Fontenay Drive, Louisville")
flower.create_flower_border(c, 5 * inch, 5 * inch, 0.2*inch, 0.3*inch)
c.save()
