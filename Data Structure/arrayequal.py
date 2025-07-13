def checkArrayEqual(arr1,arr2):
    arr1_sort = arr1.sort()
    arr2_sort = arr2.sort()
    
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    
    if arr1_len != arr2_len:
        return False
    
    for i in range(arr1_len):
        if arr1[i] != arr2[i]:
            return False
        
    return True

if __name__ == '__main__':
    # define array
    arr1 = [1, 7, 1]
    arr2 = [7, 7, 1]
    
    result = checkArrayEqual(arr1,arr2)
    
    if result == True:
        print("Array are equal")
    else:
        print("Array are not equal")