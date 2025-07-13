from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors

def draw_flower(canvas, x, y, size, color=colors.red):
    canvas.setFillColor(color)
    # Petals (example using circles)
    for i in range(8):  # 8 petals
        angle = i * 3.14159 * 2 / 8
        petal_x = x + size * 0.3 * cos(angle)
        petal_y = y + size * 0.3 * sin(angle)
        canvas.circle(petal_x, petal_y, size * 0.15, fill=1)
    # Center of flower
    canvas.setFillColor(colors.yellow)
    canvas.circle(x, y, size * 0.1, fill=1)

def create_flower_border(c, page_width=8.5*inch, page_height=11*inch, flower_size=0.3*inch, border_margin=0.5*inch):
    
    # Top border
    x = border_margin
    while x < page_width - border_margin:
        draw_flower(c, x, page_height - border_margin, flower_size)
        x += 1.5 * flower_size  # Adjust spacing as needed

    # Bottom border
    x = border_margin
    while x < page_width - border_margin:
        draw_flower(c, x, border_margin, flower_size)
        x += 1.5 * flower_size

    # Left border
    y = border_margin + 1.5 * flower_size
    while y < page_height - border_margin - 1.5 * flower_size:
        draw_flower(c, border_margin, y, flower_size)
        y += 1.3 * flower_size
        
    # Right border
    y = border_margin + 1.5 * flower_size
    while y < page_height - border_margin - 1.5 * flower_size:
        draw_flower(c, page_width - border_margin, y, flower_size)
        y += 1.3 * flower_size
        
    

from math import sin, cos

if __name__ == "__main__":
    c = canvas.Canvas("flower_border.pdf")
    create_flower_border(c)
    c.save()