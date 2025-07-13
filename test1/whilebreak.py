mylist = [1, 2, 3]
i = 0
while i < len(mylist):
    if i == 2:
        break
    print(mylist[i])
    i += 1
else:
    print("while else")
