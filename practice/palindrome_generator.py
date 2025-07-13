def is_palindrome(number: int) -> bool:
    if number // 10 == 0:
        return False
    
    temp = number
    reverse_number = 0

    while temp != 0:
        reverse_number = (10 * reverse_number) + (temp % 10)
        temp = temp // 10
    
    if number == reverse_number:
        return True
    else:
        return False


def palindrome_generator(stop=0) -> int:
    i = 1
    while i <= stop:
        if is_palindrome(i):
            yield(i)
        i += 1


palindrome_iter = iter(palindrome_generator(1000))
# for i in palindrome_iter:
#     print(i, end=",")

print(next(palindrome_iter))
print(next(palindrome_iter))
print(next(palindrome_iter))
# a = ()


