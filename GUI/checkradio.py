import tkinter
from tkinter import *

win = Tk()

music_value = IntVar()
video_value = IntVar()
music = Checkbutton(win, text = "Music",offvalue=0,onvalue=1,variable=music_value)
video = Checkbutton(win, text = "Video",offvalue=0,onvalue=1,variable=video_value)
music.pack()
video.pack()

option_value = IntVar()

yes = Radiobutton(win, text = "Yes",variable=option_value,value=1)
no = Radiobutton(win, text = "No",variable=option_value,value=2)
other = Radiobutton(win, text = "Other",variable=option_value,value=3)
yes.pack()
no.pack()
other.pack()


win.mainloop()