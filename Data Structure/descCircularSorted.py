def checkDescCircularSorted(array):
    cnt = 0
    # length of array
    array_len = len(array)
    
    for i in range(array_len - 1):
        if array[i] < array[i + 1]:
            cnt += 1

    if cnt == 1:
        return array[0] < array[array_len - 1]
    else:
        return False
        
if __name__ == '__main__':
    # Given array
    array = [9, 5, 3, 35, 26, 11]
    
    # call function to decide if it is circular sorted array
    result = checkDescCircularSorted(array)
    
    if result == True:
        print(f"{array} <- Array is in Descending circular sorted array")
    else:
        print(f"{array} <- Array is not in Descending circular sorted array")