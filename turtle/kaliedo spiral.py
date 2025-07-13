import turtle as tr
import time as ti
# from enum import Enum
from itertools import cycle

colors=cycle(['red','yellow','blue','green','purple','grey','pink'])

def draw_shape(shape,radius,i,fwd=0):
    fwd += 2
    t.forward(fwd)
    t.color(next(colors))
    t.right(10)
    if shape == "circle":
        t.circle(radius)
        draw_shape("square",radius + 5, i + 1,fwd)
    else:
        for i in range(4):
            t.forward(1.75 * radius)
            t.left(90)
        draw_shape("circle",radius + 5, i + 1,fwd)   
tr.bgcolor("dodger blue")
t = tr.Turtle()
draw_shape("circle",5,1)