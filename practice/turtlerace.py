import turtle as tr
import random
import tkinter as tk

player_one = tr.Turtle()
player_one.shape("turtle")
player_one.lt(90)
player_two = player_one.clone()
player_two.color("blue")

player_one.color("red")
player_one.penup()
player_one.goto(-200,-100)

player_two.shape("turtle")
player_two.penup()
player_two.goto(200,-100)

player_one.goto(-170,300)
player_one.pendown()
player_one.circle(30)
player_one.penup()
player_one.goto(-200,-100)

player_two.goto(230,300)
player_two.pendown()
player_two.circle(30)
player_two.penup()
player_two.goto(200,-100)
player_one_win = False
player_two_win = False
player_one.pendown()
player_two.pendown()
for i in range(20):

    player_one_chance = random.randint(1,6)
    player_one_chance = player_one_chance * 10
    player_one.fd(player_one_chance)
    if player_one.ycor() >= 300:
        player_one_win = True
        break
        
    player_two_chance = random.randint(1,6)
    player_two_chance = player_two_chance * 10
    player_two.fd(player_two_chance)

    if player_two.ycor() >= 300:
        player_two_win = True
        break

if player_one_win:
    print("Player one win")
else:
    print("Player two win")

tk.mainloop()