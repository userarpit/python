from decorator import debug, timer, repeat

@timer
class Book:
    @debug
    def __init__(self, title, author, publication_year):
        print("a")
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        print("b")
        return (
            f"{self.title} is written by {self.author} in year {self.publication_year}"
        )

    def __call__(self):
        print("call")
    # def __repr__(self):
    #     class_name = type(self).__name__
    #     return f"{class_name}({self.title!r},{self.author!r},{self.publication_year})"


b = Book("Python trics", "Dan Bader", 2009)
# print(f"{b = !s}")
# c = eval(repr(b))
# print(type(c))
# print(b)

# greet = repeat(4)(greet)
@repeat(num_times=4)
def greet(name):
    print(f"{name}")

# say_whee = repeat(say_whee)
@repeat
def say_whee(name):
    print(name)

greet("a")
say_whee("arpit")
b()