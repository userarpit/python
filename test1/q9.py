list1 =  [12,24,35,24,88,120,155,88,120,155]

no_dup = []
for x in range(len(list1)):
    if list1[x] not in no_dup:
        no_dup.append(list1[x])

no_dup.reverse()
print(no_dup)
