def is_prime(num):
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            return False
    return True    

def main():
    num = int(input("Enter Number - "))        
    if is_prime(num):
        print("Number is prime")
    else:
        print("Number is not prime")
# print(__name__)
if __name__ == "__main__":
    main()