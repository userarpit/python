import turtle as tr
import tkinter as tk
import time
import sys
t = tr.Turtle()
t.speed('slow')
t.penup()    
def rec(length,width,color,direction):
    t.pendown()
    t.color(f"{color}")
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        direction(90)
        t.forward(width)
        direction(90)
    t.end_fill()
    t.penup()

def goto_draw_rectangle(goto_x, goto_y, length, width, color, direction):
    t.goto(goto_x,goto_y)
    rec(length,width,color,direction)
# head
goto_draw_rectangle(-90,130,80,40,"red",t.left)
# eye section
goto_draw_rectangle(-70,150,40,10,"white",t.left)
# eyes
goto_draw_rectangle(-65,150,5,5,"black",t.left)
goto_draw_rectangle(-40,150,5,5,"black",t.left)
# mouth
t.right(5)
goto_draw_rectangle(-75,135,50,5,"black",t.left)
t.left(5)
# neck
goto_draw_rectangle(-60,100,20,30,"grey",t.left)
# body
goto_draw_rectangle(-110,100,120,200,"red",t.right)

# left arm
goto_draw_rectangle(-170,50,60,20,"grey",t.left)
# left hand
goto_draw_rectangle(-185,50,15,50,"grey",t.left)
# right arm
goto_draw_rectangle(10,50,60,20,"grey",t.left)
# right hand
goto_draw_rectangle(70,50,15,50,"grey",t.left)

# left leg
goto_draw_rectangle(-80,-100,20,90,"grey",t.right)
# right leg
goto_draw_rectangle(-40,-100,20,90,"grey",t.right)
# left leg bottom
goto_draw_rectangle(-120,-210,65,20,"dodger blue",t.left)
# right leg bottom
goto_draw_rectangle(-45,-210,65,20,"dodger blue",t.left)

t.hideturtle()
time.sleep(5)
sys.exit(0)
# tk.mainloop()