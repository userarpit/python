def reverse_str(str):
    # return (str[::-1])
    i = 0
    list_str = list(str)
    last = len(list_str) - 1
    while i < int(len(list_str) / 2):
        list_str[i], list_str[last] = list_str[last], list_str[i]
        i += 1
        last -= 1
    return "".join(list_str)


print(reverse_str("knh sdikhaio hdlandlkjsd"))
list_ = [1,2,3,4,5,6,7,8,9]
list_.reverse()
print(list_)

