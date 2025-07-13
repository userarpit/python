list1 = [{10: 1}, {1: 20}, {2: 23}]
print(list1)

# print(sorted(list1))
for i in list1:
    for k, v in i.items():
        print(k)


def find_highest_value(key):
    value_list = []
    for i in list1:
        if key == list(i.keys())[0]:
            value_list.append(i[key])
    if value_list:
        return max(value_list)
    else:
        return "key not present"


print(find_highest_value(5))
