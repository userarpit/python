number_generator = (x for x in range(10))

# fibonacci_generator = (
#     x if x < 2 else fibonacci_generator[x - 1] + fibonacci_generator[x - 2]
#     for x in range(10)
# )

def fibonacci_generator():
    a, b = 0, 1
    for _ in range(10):
        yield a
        a, b = b, a + b
        
fib = fibonacci_generator()
for n in fib:
    print(n)  # This will print numbers from 0 to 9
