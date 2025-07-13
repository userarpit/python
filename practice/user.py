class User:
    pass


u = User()
u.name = "Arpit"
setattr(u, "age", 38)
print(u.__dict__)
