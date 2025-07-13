with open("number.txt","r") as file:
    data = file.readlines()

print(data)
total = sum(int(i.strip()) for i in data)
print(total)