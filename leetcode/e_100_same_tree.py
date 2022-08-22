
def is_same_dfs_iteratively(p, q):
    ps = [p]
    qs = [q]

    if p is None and q is None:
        return True

    while len(ps) > 0 and len(qs) > 0:
        pnode = ps.pop()
        qnode = qs.pop()

        if pnode is None or qnode is None:
            return False

        if pnode.val != qnode.val:
            return False
        
        if pnode.right or qnode.right:
            ps.append(pnode.right)
            qs.append(qnode.right)
        
        if pnode.left or qnode.left:
            ps.append(pnode.left)
            qs.append(qnode.left) 
    return True

# dfs recursively
def is_same_dfs_recurse(p, q):

    if p is None and q is None:
        # we have made it to a leaf node
        return True

    # check for differences between curr nodes    
    if p is None or q is None or \
        p.val != q.val:
        return False

    # recurse
    left = is_same_dfs_recurse(p.left, q.left)
    right = is_same_dfs_recurse(p.right, q.right)

    return left and right



class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

p = TreeNode(2)
p.left = TreeNode(1)
p.right = TreeNode(3)

q = TreeNode(2)
q.left = TreeNode(1)
q.right = TreeNode(3)

# p = TreeNode(1)
# p.left = TreeNode(2)

# q = TreeNode(1)
# q.right = TreeNode(2)



print(is_same_dfs_iteratively(p, q))
print(is_same_dfs_recurse(p,q))