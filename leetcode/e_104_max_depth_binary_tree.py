'''

'''
def maxDepth(root):
    if root is None:
        return 0
    
    return dfs((root, 1))

def dfs(self, node):
    n, curr_depth = node
    
    if n is None:
        return

    depth_left = self.dfs((n.left, curr_depth+1))
    depth_right = self.dfs((n.right, curr_depth+1))
    return max(depth_left, depth_right, curr_depth)


# breath first search iteratively
from collections import deque

def max_depth_bfs_iteratively(root):
    if not root:
        return 0

    q = deque([root])
    max_level = 0
    while q:
        for _ in range(len(q)):
            curr_node = q.popleft()
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        max_level += 1
    return max_level

# depth first search iteratively
def max_depth_dfs_iteratively(root):
    if not root:
        return 0

    s = [(root,1)]
    max_depth = 0
    while s:
        n, d = s.pop()
        max_depth = max(max_depth, d)
        if n.right:
            s.append((n.right, d+1))
        if n.left:
            s.append((n.left, d+1))
    return max_depth



