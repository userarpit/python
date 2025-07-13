import tkinter as tk

window = tk.Tk()
text1 = tk.Text(window)
text1.pack()
def printletter(text1):
    print(text1.get("1.0",tk.END))

def remove(text1):
    text1.delete("1.0","1.2")

get_button = tk.Button(text = "print",command=lambda:printletter(text1))
get_button.pack()

button = tk.Button(text = "Remove",command=lambda:remove(text1))
button.pack()

window.mainloop()