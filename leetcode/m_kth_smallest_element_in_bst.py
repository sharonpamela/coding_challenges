'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of all the 
values of the nodes in the tree.
'''

def kthSmallest(root, k):
    # do an in-order traversal of the tree
    # this returns the nodes in order
    res = []
    in_order_traversal(root, res)
    if len(res) >= k-1:
        return res[k-1]
    else:
        return -1

def in_order_traversal(root, res):
    if root.left:
        in_order_traversal(root.left)
    res.append(root.val)
    if root.right:
        in_order_traversal(root.right)