class SameEqualHash:
    def __init__(self, name):
        self.name=name

    def __eq__(self, other):
        return True

    def __hash__(self):
        return 42

print(SameEqualHash("a") == SameEqualHash("a"))
# print(hash(SameEqualHash()))
# print(hash(SameEqualHash()))
# print(id(SameEqualHash()))  
# print(id(SameEqualHash()))