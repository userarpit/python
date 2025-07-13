name: str = "arpit"
print(name)

last_name: str = "Khandelwal"
first_name: str


def capital(name: str) -> str:

    # print(last_name.__annotations__)
    # name=3
    return f"{name.upper()} {last_name}"
    # return None


print(capital("arpit"))
print(capital.__annotations__)
# print(reveal_type(math.pi))

# print()
