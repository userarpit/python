list1 = [12,24,35,70,88,120,155]

no_5_and_7 = [x for x in list1 if not (x % 5 ==0 and x % 7 ==0)]
print(no_5_and_7)
