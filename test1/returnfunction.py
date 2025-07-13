''' return a function'''
def create_add(a : int):
    '''define function and returned it'''
    def addition(b:int) -> int:
        '''return -> sum of 2 variables'''
        return a + b
    
    return addition

testadd = create_add(10) # a = 10

print(testadd(20)) # pass va;ue of b
print(create_add.__doc__)
print(testadd.__doc__)