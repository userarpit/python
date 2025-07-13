gene_expr = [x * x for x in range(10)]
print(gene_expr)
print(type(gene_expr))

for g in gene_expr:
    print(g, end=" ")


def vector(*args):
    for a in args:
    #     print(a, end=",")
        print(f"{a}", end=" ")

print()
vector(*gene_expr)

print(type(None))

def a():
    pass

print(a())