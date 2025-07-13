from tkinter import *


win = Tk()
win.geometry("400x400")
def b_func():
    print("hi")

b = Button(win, text="click me",font=4,wraplength=100,command=b_func,pady=10)
# b.pack()
# b.grid(row=1,column=2)
b.place(x=100,y=200)


b1 = Button(win, text="click me111")
# b1.pack()
# b1.grid(row=2,column=1)
b1.place(x=400,y=600)

win.mainloop()