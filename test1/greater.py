a = 10
b = 30
print ((lambda:a, lambda:b) [b > a]())
