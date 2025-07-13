
number = 28

def findandsumofdivisior(number):
    '''find divisor of the number and return as list'''
    total = 1
    i = 2
    while i * i <= number:
        if number % i == 0:
            total = total + i + (number / i)
        i += 1
    return total

def isPerfect(number):
    return findandsumofdivisior(number) == number

if __name__ == "__main__":
    for number in range(10000):
        if isPerfect(number):
            print(number)