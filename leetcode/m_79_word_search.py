'''
Given an m x n grid of characters board and a string word, 
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally 
or vertically neighboring. 
The same letter cell may not be used more than once.
'''
from collections import deque
def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    path = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or \
            r >= rows or c >= cols or \
                word[i] != board[r][c] or \
                    (r,c) in path:
                    return False
        path.add((r,c))
        res = (dfs(r + 1, c, i + 1) or
            dfs(r - 1, c, i + 1) or
            dfs(r, c - 1, i + 1) or
            dfs(r, c + 1, i + 1))
        path.remove((r,c))
        return res

    for row in range(rows):
        for col in range(cols):
            res = dfs(row, col, 0)
            if res:
                return True
    return False

       

board = [["A","B","C","E"],["N","F","C","S"],["A","D","E","E"]]
word = "SEE"

board = [
["A","B","C","E"],
["S","F","E","S"],
["A","D","E","E"]]
word ="ABCESEEEFS"
print(exist(board, word))



'''
The solution below passes most tests but not all
'''
# def exist(board, word):
#     rows = len(board)
#     cols = len(board[0])
#     start_char = word[0]

#     def bfs(row, col):
#         visited = set()
#         directions = [[-1,0], [1,0], [0,1], [0,-1]]
#         q = deque()
#         q.append((row, col))
#         visited.add((row, col))
#         chars = deque([ l for l in word])
#         while q:
#             r,c = q.popleft()
#             # check if the current char is the next char needed
#             if board[r][c] == chars[0]:
#                 chars.popleft()
#                 if len(chars) == 0:
#                     return True

#             # examine all next possible char positions
#             for dr,dc in directions:
#                 dr = r+dr
#                 dc = c+dc
#                 next_char = chars[0]

#                 if dr in range(len(board)) and \
#                     dc in range(len(board[0])) and \
#                     (dr,dc) not in visited and \
#                     board[dr][dc] == next_char:
#                         q.append((dr,dc))
#                         print(f"queue: {q}")
#             visited.add((r,c))      
#         return False  

#     for row in range(rows):
#         for col in range(cols):
#             print(f"{row} {col}")
#             print(f"{board[row][col]} == {start_char}")
#             if board[row][col] == start_char:
#                 res = bfs(row, col)
#                 if res:
#                     return True
#     return False