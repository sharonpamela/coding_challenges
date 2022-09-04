''''
A path in a binary tree is a sequence of nodes 
where each pair of adjacent nodes in the 
sequence has an edge connecting them. A node 
can only appear in the sequence at most once. 
Note that the path does not need to pass through 
the root.

The path sum of a path is the sum of the node's 
values in the path.

Given the root of a binary tree, return the 
maximum path sum of any non-empty path.
'''
from turtle import right


def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0

        left_max = dfs(root.left)
        right_max = dfs(root.right)
        left_max = max(left_max, 0)
        right_max = max(right_max, 0)

        res[0] = max(res[0], root.val + left_max + right_max)

        return root.val + max( left_max, right_max)

    dfs(root)
    return res[0]