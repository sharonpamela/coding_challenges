class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root: return True
        if not subRoot: return False

        if self.sameTree(root, subRoot):
            return True
        
        return (self.isSubTree(root.left, subRoot.left) or
        self.isSubTree(root.right, subRoot.right)) 



    def sameTree(self,s,t):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))
        
        return False