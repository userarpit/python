x = set(["a", "b", "a"])
print(x)

# first_name_set = set("arpit")
# last_nane_set = set()

x1 = {"foo", "bar", "baz"}
x2 = {"baz", "qux", "quux"}

print(x1 | x2)

print(x1.union(x2))

print(x1.union(("a", "b")))
print(x1.intersection(x2))
print(x1 & x2)
print(x1.intersection(["a", "baz"]))

d = {1, 2}
a = {1, 2, 3, 30, 300}
b = {30, 40, 50, 60}
c = {100, 200, 300, 60}

print(a - b - c)

# print(x1.symmetric_difference(x2))
print(x1 ^ x2)  # return all elements except common
print(a ^ b ^ c)  # do a ^ b, first, and then result(1,b) with c

# print()
print(x1.isdisjoint(a))
print(x1.isdisjoint(x2))

print(d.issubset(a))

print(d < a)  # d is proper subset of a
print(a.issuperset(d))  # a is superset of d
print(a > d)  # a is proper superset of d

a = a & d
print(a)
print(b)
print(c)
print(b.intersection_update(c))  # in place update
print(b)
c.difference_update(b)
print(c)

a = set(list(range(1, 10)))
b = set(list(range(1, 10, 2)))
print(a)
print(b)
print(id(a))
a ^= b
print(a)
print(id(a))

# using augmented operator , set are modified in place, while frozen set are not modified in place, new object gets created

# a.add(44)
# print(a)
# a.discard(81)
# print(a)
# print(a.pop())
# print(a.pop())
# a.clear()
# print(b)

# # frozenset
# x = frozenset([1,2,3])
# print(x)
# # print(a)?
# # print(x.add(4))
# print(id(x))
# x |= b
# print(x)
# print(id(x))

x = frozenset({1, 2, 3})
y = frozenset({"a", "b"})

d = {x: "foo", y: "bar"}
print(d)
