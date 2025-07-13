def is_prime(num):
    for i in range(2, int(num/2)):
        if num % i == 0:
            return False
    return True


for i in range(2, 50):
    if is_prime(i):
        print(i, end=" ")
