import turtle as t
import time as ti
import random as r
import sys

t.bgcolor("yellow")

caterpiller = t.Turtle()
caterpiller.shape('turtle')
caterpiller.speed(0)
caterpiller.penup()
caterpiller.hideturtle()

leaf = t.Turtle()
leaf_shape=((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()

text_turtle=t.Turtle()
text_turtle.write("Press space to start",align="center",font=('Arial',18,'bold'))
text_turtle.hideturtle()
                  
score_turtle=t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)
score_turtle.penup()
score_turtle.goto(300,300)

def outside_window():
        
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2

    (x,y) = caterpiller.pos()
    if x < left_wall or x > right_wall or y > top_wall or y < bottom_wall:
        return True
    else:
        return False

def place_leaf():
    leaf.hideturtle()
    x = r.randint(int(-t.window_width() / 2),int(+t.window_width() / 2))
    y = r.randint(int(-t.window_height() / 2),int(+t.window_height() / 2))
    leaf.goto(x,y)
    leaf.showturtle()
    return x,y

def game_over():
    
    answer = t.Screen().textinput("Game Over","Press 'Y/y' to Continue, 'N/n' to Exit")
    if answer in ['Y','y']:
    
        caterpiller.hideturtle()
        caterpiller.home()
        score_turtle.clear()
        leaf.clear()
        caterpiller.speed(0)
        caterpiller.shape('turtle')
        caterpiller.shapesize(1.0,1.0,1.0)
        listen_keys()        
        start_game()
    else:
        sys.exit(0)

def update_score(score):    
    score_turtle.clear()
    score_turtle.write("Score :" + str(score),align="center",font=('Arial',18,'bold'))

def start_game():
    text_turtle.clear()
    caterpiller.showturtle()
    caterpiller.speed(1)
    x,y=place_leaf()
    
    i=1
    width, height, outline = caterpiller.shapesize()
    score = 10
    while True:
        caterpiller.fd(10)
        if outside_window():
            game_over()

        if caterpiller.distance(leaf) < 20:
            update_score(score)
            score += 10
            place_leaf()
            width, height, outline = caterpiller.shapesize()
            i += 0.0002
            caterpiller.speed(i)
            caterpiller.shapesize(width,height +1,outline)

def up():
    if caterpiller.heading() == 0 or caterpiller.heading() == 180:
        caterpiller.setheading(90)

def down():
    if caterpiller.heading() == 0 or caterpiller.heading() == 180:
        caterpiller.setheading(270)

def left():
    if caterpiller.heading() == 90 or caterpiller.heading() == 270:
        caterpiller.setheading(180)

def right():
    if caterpiller.heading() == 90 or caterpiller.heading() == 270:
        caterpiller.setheading(0)

def listen_keys():
    t.listen()
    t.onkey(start_game,'space')
    t.onkey(up,'Up')
    t.onkey(down,'Down')
    t.onkey(left,'Left')
    t.onkey(right,'Right')

listen_keys()

t.mainloop()