def decorator(cls):
    class NewClass(cls):
        attr = 100
    return NewClass

@decorator
class X:
    pass

# X = decorator(X)

@decorator
class Y:
    pass

# Y = decorator(Y)
@decorator
class Z:
    pass

# Z = decorator(Z)

print(X.attr)