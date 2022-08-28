'''
Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal 
of the same tree, construct and return the binary tree.
'''

def buildTree(self, preorder, inorder):
    # preorder tells root location index 0 
    # inorder tells left and roght nodes in the tree 
    # based on nodes to the left and right of root node

    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1], inorder[mid+1])
    return root
