import threading as th

def print_cube(x: int) -> int:
    print(x ** 3)

def print_square(x: int) -> int:
    print(x ** 2)    

def main():
    t1 = th.Thread(target=print_cube,args=(3,))
    t2 = th.Thread(target=print_square,args=(3,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")

if __name__ == "__main__":
    main()