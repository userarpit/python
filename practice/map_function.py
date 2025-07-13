import math

words = ["apple", "banana", "cherry", "elderberry"]

# len_words = map(len, words)

filter_words = filter(lambda x: len(x) > 5, words)

print(list(filter_words))


def integers():
    for i in range(1, 10):
        yield i


int_iter = integers()
square = map(math.pow, integers(), range(1, 10))
print(list(square))

print("custom zip")

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

my_zip = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(my_zip)






