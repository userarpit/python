list1 = [12,24,35,70,88,120,155]

index = [list1[i] for i in range(len(list1)) if i not in [0,4,5]]
print(index)  
