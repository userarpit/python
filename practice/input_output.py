# 3[a]2[bc]

s = "2[ac5[b]]"


def decodeString(s):
    stack = []
    # breakpoint()
    for c in s:
        if c.isnumeric():
            stack.append(c)
        elif c == "[":
            stack.append(c)
        elif c.isalpha():
            stack.append(c)
        elif c == "]":
            print_char = []
            while stack[-1] != "[":
                print_char.append(stack.pop())

            print_char.reverse()
            combined_string = "".join(char for char in print_char)
            # print(combined_string)
            stack.pop()
            num = int(stack.pop())
            # print(num)
            if len(stack):
                stack.append(str(combined_string) * num)
                continue
            
            print(f"{str(combined_string) * num}", end="")


decodeString(s)
