def yell(string_):
    return (f"{string_.upper()} !")

print(yell("hello"))


bark = yell
del yell
print(bark("bow"))

# del yell
print(bark.__qualname__)
print(bark)

list_fun = [bark, str.lower]
print(list_fun[0]("yes"))

def func(func):
    return (func("function pass as object"))

print(func(bark))