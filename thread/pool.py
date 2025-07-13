import multiprocessing as mp
import os

def square(x):
    print("Worker process id for {0}: {1}".format(x, os.getpid()))
    return x * x

if __name__ == "__main__":
    mylist = [1,2,3,4,5]

    p = mp.Pool()

    squarelist = p.map(square,mylist)

    print(squarelist)