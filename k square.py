"""Problem Statement:

Given the row count of a square array and an integer number k,

return a 2D square array where

all diagonal elements are k and
all non-diagonal elements are 0.
Note: The returned 2D array should be of integer type.

Input Format:

Input has two lines.
First line corresponds to the row count.
Second line is the integer k.
Output Format:

A 2D square array
Sample Input:

3
300
Sample Output:

[[300, 0, 0],
 [0, 300, 0]
 [0, 0, 300]]
Note: We can use special arrays to solve this."""


#Solution

import numpy as np

def k_array(row_count, k):
    '''
    INPUT : row_count, k 
    
    OUTPUT: result -> 2D array
    '''
    
    result = None
    
    ## CODE STARTS HERE
    result = np.zeros((row_count, row_count), dtype=int)
    np.fill_diagonal(result, k)
    
    ## CODE ENDS HERE
    
    return result
