class Test:
    def __init__(self,limit):
        self.limit = limit

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.limit < 0:
            raise StopIteration
        x = self.x
        if self.x == self.limit:
            raise StopIteration

        self.x += 1
        return x

for i in Test(3):
    print(i , end=" ")