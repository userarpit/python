d = locals()
print(type(d))
keys = list(d.keys())
values = list(d.values())


for i,j in zip(keys,values):
    print(i,end=" ")
    print(j)


def localsPresent():
    present = True
    print(present)
    locals()['present'] = False;
    print("***")
    print(locals().keys())
    print("***")
    print(present)

localsPresent()

print(locals().keys())