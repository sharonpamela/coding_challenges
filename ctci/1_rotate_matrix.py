'''
Rotate Matrix: Given an image represented by an NxN matrix, 
where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees.
Can you do this in place?
'''
import math
import unittest

def rotate_matrix(matrix):
    '''
    this approach takes advantage of the fact that transposed matrices
    have the same diagonal as the orig matrix. so it swaps the values
    above the diag with the values below the diagonal.

    space complexity O(1) as swap is done in-place with no extra temp arrays.
    time complexity O(NxN) as all N^2 elems are visited and there is no way to
    traspose without this action.
    '''
    rows = n = len(matrix)
    cols = len(matrix[0])
    if ( rows == 0 or rows != cols ):
        raise ValueError("Matrix provided has no rows or is not an nxn matrix.")

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    

class Test(unittest.TestCase):
    def test1(self):
        m = [[2,3],[4,5]]
        expected = [[2, 4], [3, 5]]
        rotate_matrix(m)
        self.assertEqual(expected,m)

    def test2(self):
        m = [[1,1,1],[2,2,2],[3,3,3]]
        expected = [[1,2,3], [1,2,3], [1,2,3]]
        rotate_matrix(m)
        self.assertEqual(expected,m)

    def test3(self):
        m = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
        expected = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]
        rotate_matrix(m)
        self.assertEqual(expected,m)

    def test_invalid_matrix(self):
        m = [[2,3,1],[4,5,1]]
        with self.assertRaises(Exception):
            rotate_matrix(m)
        
    def test_empty_matrix(self):
        m = []
        with self.assertRaises(Exception):
            rotate_matrix(m)
    

unittest.main(verbosity=2)

# rotation approach
# def rotate_matrix(matrix):
#     rows = n = len(matrix)
#     cols = len(matrix[0])
#     if ( rows == 0 or rows != cols ): return False

#     for layer in range(math.floor(n / 2)):
#         first = layer
#         last = n - 1 - layer
#         for i in range(first, last):
#             offset = i - first

#         top = matrix[first][i] # save top row
        
#         # left -> top
#         matrix[first][i] = matrix[last - offset][first]
        
#         # bottom -> left
#         matrix[last - offset][first] = matrix[last][last - offset]
        
#         # right -> bottom
#         matrix[last][last - offset] = matrix[i][last]

#         # top -> right
#         matrix[i][last] = top # right<- saved top
#     return True
