'''
Given the root of a binary tree, return the level order traversal 
of its nodes' values. (i.e., from left to right, level by level).
'''


from collections import deque


def level_order_traversal(root):

    q = deque()
    q.append((root,1))
    res = []

    while q:
        node = q.popleft()
        res.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res


