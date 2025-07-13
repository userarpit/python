def infinite_sequence(end=0) -> int:
    num = 0
    while num < end:
        yield int(num)
        num += 1


# for i in infinite_sequence():
#     print(i, end=" ")


is_iter = iter(infinite_sequence(end=10))

for item in is_iter:
    print(item, end= " ")