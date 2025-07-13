# import os
file1 = open(r"conda.txt", "r")
file2 = open("abc.txt", "w")

for line in file1.readlines():
    print(line)
    file2.write(line)

file1.close()
file2.close()

