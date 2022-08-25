'''
Given an n x n binary matrix grid, return the length of the shortest clear 
path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) 
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., 
they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

example:
Input: grid = [[0,1],[1,0]]
Output: 2
'''

import collections


def find_minimum_path(matrix):
    if matrix[0][0] == 1 or matrix[-1][-1] == 1:
        return -1

    # first tile counts
    path_len = 1

    # set starting position as "seen"
    matrix[0][0] = 1

    directions = [(0,1),(0,-1),(-1,0),(1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
    q = collections.deque([(0,0,path_len)])

    while q:
        x,y,curr_len = q.popleft()

        # check to see if i have arrived at bottom right corner
        if (x,y) == (len(matrix)-1, len(matrix[0])-1):
            return curr_len

        for dx,dy in directions:
            deltaX = x+dx
            deltaY = y+dy
            # check if current position is within bounds
            # and ignore positions where "1" is present
            if (0 <= deltaX < len(matrix)) and (0 <= deltaY < len(matrix[0])) and not matrix[deltaX][deltaY]:
                # set current position to "seen" to prevent loop
                matrix[deltaX][deltaY] = 1
                
                # add valid positions to queue with +1 len
                q.append((deltaX, deltaY, curr_len+1))

    return -1

print(find_minimum_path([[0,1],[1,0]]))