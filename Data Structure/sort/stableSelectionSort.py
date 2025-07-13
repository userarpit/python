
def stableSelectionSort(array):
    len_array = len(array)
    
    for i in range(len_array):
        
        min_index = i
        # get minimum
        for j in range(i + 1,len_array):
            if array[min_index] > array[j]:
                min_index = j

        # insert minimum at ith index
        value = array[min_index]
        while min_index > i:
            array[min_index] = array[min_index - 1]
            min_index -= 1
            
        array[i] = value
    
    return array
       
# Driver code
if __name__ == '__main__':
    array = [4, 5, 3, 3, 4, 1]   # length = 6
    
    print("Stable sorted array",stableSelectionSort(array)) 
    