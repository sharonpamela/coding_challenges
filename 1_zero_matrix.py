'''
Zero Matrix: Write an algorithm such that if an element in 
an MxN matrix is 0, its entire row and column are set to 0. 
'''
import unittest

def zero_matrix(matrix):
    columns_to_zero_out = []

    m = len(matrix) #rows
    n = len(matrix[0]) #cols

    if not m:
        raise Exception("The matrix can't be empty")

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                # this row needs to be zeroed out
                matrix[i] = [ 0 ] * n
                columns_to_zero_out.append(j)
                # skip the rest of the row
                break
    
    # zero out all previously flagged columns
    for row in range(len(matrix)):
        for col in columns_to_zero_out:
            matrix[row][col] = 0



class Test(unittest.TestCase):
    def test1(self):
        m = [[2,0],[4,5]]
        expected = [[0,0], [4, 0]]
        zero_matrix(m)
        self.assertEqual(expected,m)

    def test2(self):
        m = [[1,1,1],[2,0,2],[3,3,3]]
        expected = [[1,0,1], [0,0,0], [3,0,3]]
        zero_matrix(m)
        self.assertEqual(expected,m)

    def test3(self):
        m = [[1,1,1,1,1],[2,2,2,0,2],[3,3,3,3,3],[4,0,4,4,4],[5,5,5,5,5]]
        expected = [[1,0,1,0,1],[0,0,0,0,0],[3,0,3,0,3],[0,0,0,0,0],[5,0,5,0,5]]
        zero_matrix(m)
        self.assertEqual(expected,m)

    def test_empty_matrix(self):
        m = []
        with self.assertRaises(Exception):
            zero_matrix(m)

unittest.main(verbosity=2)