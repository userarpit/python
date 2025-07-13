import pickle

class foobar:
    def __init__(self, x):
        print("init")
        self.x = x
        self.c = lambda y: y * y

    def __repr__(self):
        print("repr")
        return f"foobar({self.x})"
    
    def __getstate__(self):
        print("getstate")
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes
    
    def __setstate__(self, state):
        print("setstate")
        print("state :",state)
        self.__dict__.update(state)
        self.c = lambda y: y * y
        
if __name__ == "__main__":
    my_foobar = foobar(10)
    print(my_foobar.__dict__)
    my_pickle_string = pickle.dumps(my_foobar)
    print("between")
    # print(my_pickle_string.__dict__)
    my_unpickle_string = pickle.loads(my_pickle_string)
    print(my_unpickle_string.__dict__)