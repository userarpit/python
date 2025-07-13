import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return
    
    txt_edit.delete("1.0", tk.END)

    with open(filepath, mode="r") as input_file:
        data=input_file.read()
        txt_edit.insert(tk.END, data)

    window.title(f"Simple Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],defaultextension="txt")

    if not filepath:
        return
    
    with open(filepath, mode="w") as output_file:
        data = txt_edit.get("1.0", tk.END)
        output_file.write(data)
    
    window.title("Text Editor")

window = tk.Tk()
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.title("Text Editor")

left_frame = tk.Frame(master=window)
left_frame.grid(row=0, column=0, sticky="ns")

btn_open = tk.Button(master=left_frame, text="Open", command=open_file)
btn_open.grid(row=0, column=0, padx=10, pady=10)

btn_save = tk.Button(master=left_frame, text="Save as..", command=save_file)
btn_save.grid(row=1, column=0, padx=10, pady=10)

txt_edit = tk.Text(master=window, width=800)
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
