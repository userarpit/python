import os

file = "a.txt"

file1 = os.path.join(os.getcwd(),file)

os.remove(file1)