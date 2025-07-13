from tkinter import Tk, Label, Entry, StringVar, Button, Listbox, END
from difflib import get_close_matches
import math
from functools import reduce

operation_list = ['add','subtract','multiply','division', 'lcm','gcf','mod', 'sum','plus','diff','addition','mul','div','minus']
def calculate(question_entry,answer_listbox):
    answer_listbox.delete(0,END)
    list_ = question_entry.get().split(" ")
    operation_close_match = []
    save_number_list = []

    for item in (list_):
        if item.isnumeric():
            save_number_list.append(item)
        else:
            if isinstance(item,str) and len(item) > 0:
                close_match = get_close_matches(item.lower(),operation_list,n=1,cutoff=0.8)
                if len(close_match) != 0:
                    operation_close_match.append("".join(close_match))
    answer = {}
    
    for oper in operation_close_match:
        match oper:
            case 'add' | 'sum' | 'plus' | 'addition':
                answer[oper] = float(sum(map(int,save_number_list)))
            case 'diff' | 'subtract' | 'minus':
                answer[oper] = float(reduce(lambda x,y: int(x) - int(y), save_number_list))
            case 'mul' | 'multiply':
                answer[oper] = float(reduce(lambda x,y: int(x) * int(y), save_number_list))
            case 'division' | 'div':
                answer[oper] = float(reduce(lambda x,y: int(x) / int(y), save_number_list))
            case 'mod':
                answer[oper] = float(reduce(lambda x,y: int(x) % int(y), save_number_list))
            case 'lcm':
                answer[oper] = float(reduce(lambda x,y: math.lcm(int(x),int(y)), save_number_list))
            case 'gcf':
                answer[oper] = float(reduce(lambda x,y: math.gcf(int(x),int(y)), save_number_list))
        
    for key,value in answer.items():
        answer_listbox.insert("end",f"{key} -> {value}")
    
root = Tk()
root.resizable(width=False,height=False)
root.title("Smart Calculator")

# Set the window size
root.geometry("400x300")

# Change the background color using configure
root.configure(bg='lightskyblue')

# add label
label = Label(root,text="I am a smart calculator",padx=3,width=20,bg="white")
label.place(x=150,y=10)

# add label
name_label = Label(root,text="My name is pugger",padx=3,width=15,bg="white")
name_label.place(x=160,y=40)

# add label
what_label = Label(root,text="What can i help you",padx=3,width=15,bg="white")
what_label.place(x=160,y=130)

textin=StringVar()

question_entry = Entry(root,textvariable=textin)
question_entry.configure(width=50)
question_entry.place(x=80,y=160)


# add label
just_button = Button(root,text="Just this",padx=3,width=5,bg="white",command=lambda:calculate(question_entry,answer_listbox))
just_button.place(x=190,y=190)

# # add label
answer_listbox = Listbox(root,width=25,height=3,bg="white")
answer_listbox.place(x=140,y=230)

# c.pack()
root.mainloop()