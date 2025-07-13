from itertools import count, cycle, repeat

c = count(1)
print(next(c))
print(next(c))

color = ['red', 'green', 'blue']
color_iterator = cycle(color)
for _ in range(8):
    print(next(color_iterator))

repeat_iterator = repeat(10, times=5)
print(list(repeat_iterator))
