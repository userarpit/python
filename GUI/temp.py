import tkinter as tk

window=tk.Tk()
window.title("Temperature convertor")
window.resizable(width=False, height=False)
def convert():
    # print(int(entry_faren.get()))
    value = int(entry_faren.get()) - 32
    value = value * (5/9)
    # print(value)
    value = round(value,2)
    
    value_celcius['text'] = str(value)

entry_faren = tk.Entry(window,width=10)
entry_faren.grid(row=0,column=0,padx=5,pady=5)

label_faren = tk.Label(window,width=2,text="\N{DEGREE FAHRENHEIT}")
label_faren.grid(row=0,column=1,padx=5,pady=5)

button_faren = tk.Button(window,width=2,text="\N{RIGHTWARDS BLACK ARROW}",command=convert)
button_faren.grid(row=0,column=2,padx=5,pady=5)

value_celcius = tk.Label(window,width=4,text="")
value_celcius.grid(row=0,column=3)

label_celcius = tk.Label(window,text="\N{DEGREE CELSIUS}")
label_celcius.grid(row=0,column=4)

window.mainloop()