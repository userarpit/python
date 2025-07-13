import turtle as tr
import tkinter as tk
t = tr.Turtle()
t.color("blue")
t.speed(100)
for i in range(5,200):
    t.circle(i)

tk.mainloop()
