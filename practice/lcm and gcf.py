def lcm(a, b):
    max_num = max(a, b)
    # print(max_num)

    while True:
        if max_num % a == 0 and max_num % b == 0:
            lcm = max_num
            break

        max_num += 1

    return lcm


def gcf(a, b):
    min_num = min(a, b)

    while True:
        if a % min_num == 0 and b % min_num == 0:
            gcf = min_num
            break

        min_num -= 1

    return gcf


if __name__ == "__main__":
    a = 3
    b = 51

    print(f"LCM = {lcm(a, b)}")
    print(f"GCF = {gcf(a, b)}")
