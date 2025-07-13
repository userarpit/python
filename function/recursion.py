def summation(mylist):
    
    a = int(mylist.pop())
    """ print(a)
    print(mylist) """
    total = 0
    def sum_list(a,total):
        total += a
        if len(mylist) == 0:
            return total
        else:
            return sum_list(int(mylist.pop()),total)
    print(sum_list(a,total))

mylist = list(input("Enter numbers with space as delimiter ").split(" "))
if __name__ == "__main__":
    summation(mylist)