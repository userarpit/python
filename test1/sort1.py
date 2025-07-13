data = ((1, 2), (3, 4))
COUNT = 0
for i in data:
    COUNT += 1
    print(f"Row {COUNT} sum", sum(i))

numbers = [4,3,2,1]

numberscopy = numbers [:]
print(numberscopy)
numbers.sort()
print(numbers)