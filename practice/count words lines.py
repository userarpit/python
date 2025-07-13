with open("test1.txt","r") as file:
    a = file.readlines()
print(a)
# print(file.readline())
number_of_line = 0
total_word = 0
for line in a:
    words = sum(1 for i in line.split(" ")  if i.strip().isalpha())
    
    total_word += words
    number_of_line += 1

print(f"total word {total_word}")
print(f"total lines {number_of_line}")