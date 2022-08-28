'''
Given the root of a binary tree, determine if it is a valid 
binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less 
than the node's key.
The right subtree of a node contains only nodes with keys greater 
than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

def isValidBST(root):
    left_bound = float("-inf")
    right_bound = float("inf")

    return validate_dfs(root, left_bound, right_bound)


def validate_dfs(node, l, r):
    if not node: return True
    
    if not (node.val > l and node.val < r):
        return False
    
    l_subtree = validate_dfs(node.left,l,node.val)
    r_subtree = validate_dfs(node.right,node.val,r)
    
    return l_subtree and r_subtree
