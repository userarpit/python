def doInsertionSort(arr):
    arr_len = len(arr)
    sub_array_index = 1
    
    while sub_array_index < arr_len:
        for i in range(sub_array_index,0,-1):
            if arr[i] < arr[i-1]:
                arr[i] , arr[i-1] = arr[i-1], arr[i] 
            else:
                break
        sub_array_index += 1
        
    return arr
# driver code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6]
    print(doInsertionSort(arr))