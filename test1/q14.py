a = int(input("enter number - "))
sum = 0.0
for i in range(1,a+1):
    sum += float(i/(i+1))
print(round(sum,2))
