def quickSort(array):
    """
    Input: a list.
    Output: a sorted list.
    """
    
    # check if array is bigger than 1:
    if array==[] or len(array) == 1:
        return array
    else:
        # pivot is the index of the last element in the list: 
        pivot = len(array)-1
        k = 0
        
        # compare k-element (initially, k-index = 0) to pivot WHILE index of k-element < pivot
        # if k-element is bigger: switch elements (k-element to pivot, pivot to pivot-1, pivot-1 to k-element)
        # >>> illustration: https://prnt.sc/qcjqgw
        # if k-element is smaller: increase k-index by 1
        
        while k<pivot:
            if array[k]>=array[pivot]:
                temp1,temp2,temp3 = array[pivot],array[pivot-1],array[k]
                array[k],array[pivot-1],array[pivot] = temp2, temp1, temp3
                pivot = pivot-1
            elif array[k]<array[pivot]:
                k+=1
        # apply recursive calls for unsorted subarrays        
        array_before_pivot,array_after_pivot = array[:pivot], array[pivot+1:]
        
    return quicksort(array_before_pivot)+[array[pivot]]+quicksort(array_after_pivot)

"""
Test case:
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
"""
