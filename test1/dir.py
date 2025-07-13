import os
import time

#os.mkdir("test1")
os.chdir(r"C:\Users\HP\Desktop\Arpit\Python")
os.mkdir("test2")
print(os.getcwd())
time.sleep(6)

os.rmdir("test2")