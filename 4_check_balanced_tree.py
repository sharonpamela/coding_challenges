'''
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one. 
'''

def check_balanced(root, depth, depths):

    if root is None:
        return True

    # check if current node is a leaf
    if root.left is None and root.right is None:
        # add new depth to depths list
        if depth not in depths:
            depths.append(depth)
        
        # inspect the depths seen thus far
        if len(depths) > 2 or\
            (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
            return False
        return True

    else:

        if root.left is not None:
            left_branch = check_balanced(root.left, depth+1, depths)
            if left_branch == False:
                return False
        if root.right is not None:
            right_branch = check_balanced(root.right, depth+1, depths)
            if right_branch == False:
                return False
    return True



class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

    def insert(self, new_value):
            if self.value:
                if new_value <= self.value:
                    if self.left is None:
                        self.left = TreeNode(new_value)
                    else:
                        self.left.insert(new_value)
                elif new_value > self.value:
                    if self.right is None:
                        self.right = TreeNode(new_value)
                    else:
                        self.right.insert(new_value)
            else:
                self.value = new_value

             
root = TreeNode(5)
root.insert(2)
root.insert(8)
root.insert(1)
root.insert(3)
root.insert(4)
root.insert(6)
root.insert(9)
root.insert(7)
root.insert(10)
root.insert(1)
root.insert(1)
# root.insert(1)
# root.insert(20)
# root.insert(30)
root.PrintTree()

print(check_balanced(root, 0, []))