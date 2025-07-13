import math

def findMinandMax(array):
    
    array_len = len(array)
    min = math.inf
    max = 0
    
    for i in range(array_len - 1):
        if array[i] < min:
            min =  array[i]            
    
    for i in range(array_len - 1):
        if array[i] > max:
            max =  array[i]            
    
    return min, max

if __name__ == '__main__':
    array = [9, 5, 3, 35, 26, 11]
    
    min, max = findMinandMax(array)
    
    print(f"Minimum is {min}")
    print(f"Maximum is {max}")