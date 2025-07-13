from tkinter import *
import tkinter


win = Tk()
def sum(label,x1,x2):
    x1 = int(x1.get())
    x2 = int(x2.get())
    sum = x1 + x2
    label.config(text="sum is %d " %sum)

l1 = Label(win,text="First no")
l1.grid(row=1,column=0)

l2 = Label(win,text="Second no")
l2.grid(row=2,column=0)

label = Label(win)
label.grid(row=6,column=2)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win,textvariable=x1)
print(type(e1))
e1.grid(row=1,column=2)

e2 = Entry(win,textvariable=x2)
e2.grid(row=2,column=2)

button = Button(win,text="Calculate",command=lambda: sum(label,x1,x2))
button.grid(row=3,column=0)

win.mainloop()