'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''

from turtle import left


def rotate_img(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    # nxn matrix
    l = 0 # left bound
    r = len(matrix) - 1 # right bound

    # top left corner moves         l -> r 
    # top right corner moves        top -> bottom
    # bottom right corner moves     r -> l
    # bottom left corner moves      bottom -> top     

    while l < r:
        for i in range(r - l):
            # r - l is the number of iterations needed
            # which is 1 less than the elms in row bc 
            # rows are worked from front and end simultaneously
            top, bottom = l ,r

            # store top left for later
            top_left = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]
            
            # move top right into bottom right
            matrix[bottom][r - i] =  matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = top_left
        l += 1
        r -= 1

# another less confusing solution using transpose and reflect
'''
def rotate(matrix):
    transpose(matrix)
    reflect(matrix)
    
def transpose(matrix):
    # this means flip across the diagonal
    # 1 2 3     1 4 7
    # 4 5 6  => 2 5 8
    # 7 8 9     3 6 9
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

def reflect(matrix):
    # this means flip across vertical middle line
    # 1 4 7     7 4 1
    # 2 5 8  => 8 5 2
    # 3 6 9     9 6 3
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
'''