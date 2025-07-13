class A:
    _instance = None
    def __new__(cls, *args):
        # print("new")
        # print(cls.__name__)
        if cls._instance is None:
            cls._instance = super(A, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, value):
        self.value = value

a = A(10)
b = A(10)

a.value=30
# assert b.value == 30, "b is not 30"

print(b.value)