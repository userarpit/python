""" for i in range(1,11):
    print(8*i)
 """
map_gen = map(lambda i : 6 * i, list(range(1,11)))
for number in map_gen:
    print(number)
    