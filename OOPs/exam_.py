from string import Template

for _ in range(10):
    print("hi")

print("hi %(name)s how are you. your age 0x%(age)x" % {"name": 'arpit', "age": 381082374})
print("hi {name} how are you. your age 0x{age:x}".format(name='arpit', age=381082374))


str_ = "hi $name how are you. your age $age"
# t = Template()
print(Template(str_).substitute(name="arpit", age=hex(381082374)))

def a(a):
    # print(1)
    print(a)

# b = a
# b(44)
# # del a
# b(55)
# print(b.__name__)

# funcs = [a, str.upper]
# for f in funcs:
#     f("hi")

a = list(map(a, [3, 4, 5]))
# print(type(a))