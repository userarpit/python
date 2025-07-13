for i in range(2,1000):
    for j in range(2,i):
        if i%j == 0:
            #print(i," is not a prime number",j,"*",(int(i/j)))
            break;
    else:
        print(i," is a prime number")    