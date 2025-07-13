import math

x=0
y=0

# move up 5
y += 5


# move down 3
y -= 3

# move left 3
x -= 3

# move right 2
x += 2

distance = math.sqrt(math.pow(x,2) + math.pow(y,2))
print(distance)