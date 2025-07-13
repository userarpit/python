cat_with_hat = [False] * (100 + 1)
print(cat_with_hat)

for round in range(1, 101):
    for cat in range(1, 101):
        if cat % round == 0:
            if cat_with_hat[cat]:
                cat_with_hat[cat] = False
            else:
                cat_with_hat[cat] = True
    print(round)
    print(cat_with_hat)

for n in range(1, 101):
    if cat_with_hat[n]:
        print(n)
