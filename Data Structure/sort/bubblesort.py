
def doBubbleSort(array,array_len):
    # print(array)
    if array_len == 1:
        return array
    
    for j in range(0,array_len - 1):
        if array[j] > array[j+1]:
            array [j], array[j+1] = array[j+1], array[j]     
            
    return doBubbleSort(array, array_len-1)

if __name__ == '__main__':
    array = [6,7,3,75,43,6,2,8,5]
    array_len = len(array)
    print(doBubbleSort(array,array_len))