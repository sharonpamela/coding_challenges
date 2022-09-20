'''
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary 
diagonal and all the elements on the secondary diagonal that are 
not part of the primary diagonal.
'''
def diagonalSum(mat) -> int:
    sum = 0
    m = len(mat)
    for i in range(m):
        sum += mat[i][i] + mat[i][m-1-i]
    
    # check if added center twice
    # if matrix len is uneven, the element in the
    # middle gets added 2 times
    if m % 2 == 1:  
        sum-= mat[m//2][m//2]
    return sum

example = [ [1,2,3],
            [4,5,6],
            [7,8,9]
          ]
print(diagonalSum(example))