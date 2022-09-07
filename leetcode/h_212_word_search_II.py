'''
Given an m x n board of characters and a list of strings words, 
return all words on the board.

Each word must be constructed from letters of sequentially 
adjacent cells, where adjacent cells are horizontally or vertically 
neighboring. The same letter cell may not be used more than once in a word.
'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWordEnd = False

    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isWordEnd = True


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or \
                r == rows or c == cols or \
                    (r,c) in visited or board[r][c] not in node.children:
                    return
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWordEnd:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            visited.remove((r,c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)