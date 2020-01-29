"""
The list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
"""

def binary_search(input_array, value):
    """
    inputs: a list to search through, the value to search for.
    outputs: the index of value, or -1 if the value doesn't exist in the list.
    """
    
    result = -1
        
    if input_array!=[]:
        switch = False
        start = 0
        end = len(input_array)-1
        
        while start<=end and not switch:
            
            
            pointer = (start+end)//2
            
            if input_array[pointer]==value:
                result = pointer
                switch = True
                break
            
            elif input_array[pointer]<value:
                start = pointer+1
            
            else:
                end = pointer-1
    
    return result
    
    
"""
Test case: 
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
"""
