# print(list(filter(lambda x: x % 2 == 0, list(range(1, 21)))))
int_list = [20, 1, 3, 2, 5, 67, 45, 87, 55, 44, 66]
even_new_list = list(filter(lambda x: x % 2 == 0, int_list))
print(even_new_list)
odd_new_list = list(filter(lambda x: x % 2 != 0, int_list))
print(odd_new_list)
