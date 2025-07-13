class ObjectCounter:
    num_instance = 0
    def __init__(self):
        type(self).num_instance += 1

A = ObjectCounter()
B = ObjectCounter()

print(ObjectCounter.num_instance)

print(ObjectCounter.__dict__)