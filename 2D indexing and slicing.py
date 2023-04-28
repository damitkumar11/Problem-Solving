Problem Description:

Given a M x N array, Perform the following operations:
1. Get the odd rows from the array i.e. 1st, 3rd, 5th etc..
2. Convert the above result into 1D array and return it.
Input Format:

A 2D numpy array
Output Format:

A 1D numpy array
Sample Input:

[[1, 2, 3] 
 [4, 5, 6]
 [7, 8, 9]]
Sample Output:

[1, 2, 3, 7, 8, 9]



Solution: 

import numpy as np
def indexing(arr):
    '''
    INPUT: 
    arr -> 2D array of shape M x N

    OUTPUT: 
    result -> 1D array
    '''
    result = None
    ## Step 1: Get the odd rows from the array
    odd_row_array = arr[::2, :]

    ## Step 2: Convert it to 1D array
    result = odd_row_array.flatten()

    ## YOUR CODE ENDS HERE. MAY THE FORCE BE WITH YOU.
    return result
