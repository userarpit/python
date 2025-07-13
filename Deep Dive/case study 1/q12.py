list1 = input("Enter word separated by spaces - ").split()

no_dup = sorted(list(set(list1)))
print(" ".join(no_dup))
