from itertools import cycle

def endless():
    yield from cycle((9, 8, 7, 6))

def main() -> None:
    e = endless()
    total = 0
    for i in e:
        if total < 30:
            print(i, end=" ")
            total += i
        else:
            print()
            break
    
    print(i)

if __name__ == "__main__":
    main()
    # print



    