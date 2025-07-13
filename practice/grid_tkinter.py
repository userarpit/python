import tkinter as tk

window = tk.Tk()

# for i in range(3):
window.columnconfigure(0, weight=1, minsize=50)
window.rowconfigure([0,1], weight=3, minsize=50)
    # for j in range(3):
    #     frame = tk.Frame(
    #         master=window,
    #         relief=tk.RAISED,
    #         borderwidth=1
    #     )
        # frame.grid(row=i, column=j, padx=5, pady=5)

labela = tk.Label(master=window, text="A")
labela.grid(row=0, column=0, sticky="n")

labelb = tk.Label(master=window, text="B", bg="blue")
labelb.grid(row=1, column=0, sticky="ewns")


        # label.pack()

window.mainloop()