'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) 
node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common 
ancestor is defined between two nodes p and q as the lowest node in T 
that has both p and q as descendants (where we allow a node to be a 
descendant of itself).”

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
'''

def lowestCommonAncestor(root, p, q):

    curr = root

    # can use while loop since p and q will exist in the BST guaranteed
    while curr:

        if p.val > curr.val and q.val > curr.val:
            # p and q are under right subtree of current node
            curr = curr.right
        elif p.val < curr.val and q.val < curr.val:
            # p and q are under left subtree of current node
            curr = curr.left
        else:
            # current node is a split between p and q
            return curr