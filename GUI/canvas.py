import tkinter
from tkinter import *

win = Tk()
c = Canvas(win, height=500,width=500,bg="blue",cursor="dot")
coord = 50, 50, 240, 210
arc = c.create_arc(coord, start=45, extent=135, fill="red")
# line = c.create_line(0,0,100,100,200,100)
# line = c.create_polygon(0,0,100,100,200,100)
# oval = c.create_oval(0,0,300,200)

c.place(x=100,y=100)

win.mainloop()