size = ["small", "medium", "large", "small"]

unique_elements = sorted(list(set(size)), reverse=True)
print(unique_elements)

assigned_unique_integer = {
    element: index for index, element in enumerate(unique_elements)
}
print(assigned_unique_integer)

final_list = [(element, assigned_unique_integer[element]) for element in size]
print(final_list)
