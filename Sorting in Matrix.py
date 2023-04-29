"""You are a Teaching Assistant of the DSML course. You have access to every student’s marks in every quiz. The marks are stored in a matrix where matrix[i][j] represents the marks of the ith student in the jth quiz.
The course instructor wants you to sort the marks of students according to jth quiz in increasing order so that he can evaluate the performance of students in that particular quiz.
Here, you have to create a python program using which the instructor can sort the data on the basis of a given column(quiz). The program will return the matrix with the marks sorted in jth quiz.
The dimension of the input matrix is m× n, the output is expected to be a 2d numpy matrix of dimension mxn, but in the output the jth column must be arranged in the ascending order.
Note: The input will be 2D list not array. First convert it to array.
Input Format:
Number of test cases
For each test case, number of rows for matrix and the column to be sorted in a new line.
For each row in matrix, space separated integers are taken as input in a new line.
Output Format:
The 2D matrix, or each row in matrix space separated integers
Sample Input:
1
3 2 
5 3 9
2 1 4
7 6 8
Sample Output:
[[2 1 4]
 [5 3 9]
 [7 6 8]]
Explanation:
The 2nd column of the matrix is [3, 1, 6], the column after sorting becomes [1, 3, 6].
Note: While sorting the marks, take care of rearranging the relative order of rows too. As, [2 1 4] is a row at index 1 in the original matrix, but after sorting the 2nd column, we had to rearrange its order as mentioned in the sample output."""


#Solution


import numpy as np
def sort_marks(list2d, j):
    '''Input: arr2d= a 2d python list.
       j= integer representing the number of quiz according to which the marks need to be sorted.
       Output: a 2d numpy array.'''


    
    ans = None
    # YOUR CODE GOES HERE
    arr2d = np.array(list2d)
    #converting the list to numpy array
     
    sorted_indices_array = arr2d[:,(j-1)].argsort()
    #using argsort() function to get the indices array corresponding to the sorted (j-1)th column.

    ans = arr2d[sorted_indices_array]
    
    
    return 
