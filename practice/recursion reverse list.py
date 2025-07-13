import test1

list_ = [1,2,3,4,5,6]

def recursion(list_):
    if len(list_) == 0:
        return list_
    else:
        return recursion(list_[1:]) + list_[:1]

print(recursion(list_))

