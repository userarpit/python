from tkinter import Tk, messagebox, Canvas, Label
from itertools import cycle
from random import randrange

win = Tk()
win.title("Egg Catcher")
canvas_width = 800
canvas_heigth = 400

canvas = Canvas(win, height=canvas_heigth, width=canvas_width,background="deep sky blue")
# score_label = Label(canvas,text="Score: 0")
canvas.create_rectangle(-5,canvas_heigth-100,canvas_width + 5, canvas_heigth+5,fill = "sea green",width=0)
canvas.create_oval(-80,-80,120,120,fill="orange",width=0)

# score_label.pack()

canvas.pack()

color_cycle=cycle(['light blue','light pink','light yellow','light green','red','blue','green','black'])
egg_width=45
egg_height=55

egg_score=10
egg_speed=500
egg_interval=4000
difficulty_factor=0.95

catcher_color = 'blue'
catcher_width=100
catcher_height=100
catcher_start_x =  canvas_width / 2 - catcher_width / 2 
catcher_start_y = canvas_heigth - catcher_height-20
catcher_start_x2 = catcher_start_x + catcher_width
catcher_start_y2 = catcher_start_y + catcher_height

catcher=canvas.create_arc(catcher_start_x,catcher_start_y,catcher_start_x2,catcher_start_y2,start=200,extent=140,style='arc',outline=catcher_color,width=3)

score = 0
score_text = canvas.create_text(10,10,anchor='nw',font=('Arial',14,'bold'),fill='darkblue',text='Score : ' + str(score))

lives_remaining = 10
lives_text = canvas.create_text(canvas_width-10,10,anchor='ne',font=('Arial',14,'bold'),fill='darkblue',text='Lives: ' + str(lives_remaining))
eggs = []

def create_eggs():
    x = randrange(10,740)
    y = 40
    new_egg = canvas.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
    eggs.append(new_egg)
    win.after(egg_interval,create_eggs)

def move_eggs():
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = canvas.coords(egg)
        canvas.move(egg,0,10)
        if egg_y2 > canvas_heigth:
            egg_dropped(egg)
    win.after(egg_speed,move_eggs)

def egg_dropped(egg):
    canvas.delete(egg)
    eggs.remove(egg)
    lose_a_life()
    if lives_remaining == 0:
        messagebox.showinfo('GAME OVER','Final Score : ' + str(score))
        win.destroy()

def lose_a_life():
    global lives_remaining
    lives_remaining -= 1
    canvas.itemconfigure(lives_text,text='Lives : ' + str(lives_remaining))

def catch_check():
    (catcher_x,catcher_y,catcher_x2,catcher_y2)=canvas.coords(catcher)
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = canvas.coords(egg)
        if catcher_x < egg_x and egg_x2 < catcher_x2 and catcher_y2  - egg_y2 < 40:
            eggs.remove(egg)
            canvas.delete(egg)
            increase_score(egg_score)

    win.after(100,catch_check)

def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    egg_speed = int(egg_speed * difficulty_factor)
    egg_interval = int(egg_interval * difficulty_factor)
    canvas.itemconfigure(score_text,text='Score : ' + str(score))

def move_left(event):
    (x1,y1,x2,y2) = canvas.coords(catcher)
    if x1 > 0:
        canvas.move(catcher,-20,0)
def move_right(event):
    (x1,y1,x2,y2) = canvas.coords(catcher)
    if x2 < canvas_width:
        canvas.move(catcher,20,0)

canvas.bind('<Left>',move_left)
canvas.bind('<Right>',move_right)

canvas.focus_set()

win.after(1000,create_eggs)
win.after(1000,move_eggs)
win.after(1000,catch_check)

win.mainloop()