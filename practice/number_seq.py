def sequence(n=None):
    if n is None:
        return

    for i in range(1, n + 1):
        next = i
        line = []   
        line.append(next)
        for j in range(1, i):
            next = next + n - j
            line.append(next)

        final_line = line
        final_line.reverse()
        print_line = " ".join(str(r) for r in final_line)

        print(print_line)


if __name__ == "__main__":
    sequence(n=10)
