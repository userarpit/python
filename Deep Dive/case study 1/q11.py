lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)

text = "\n".join(lines)
print(text.upper())
