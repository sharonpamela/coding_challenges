'''
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical. 
'''
import unittest

def check_subtree(t1, t2):
    if t2 is None: return True
    return sub_tree(t1,t2)

def sub_tree(t1, t2):
    if t1 is None:
        # if main tree empty and subtree has not been found
        return False 
    elif t1.data == t2.data and match_tree(t1,t2) is True:
        # subtree root matches one of the node in t1
        # and the comparison of the entire subtree also holds true
        return True
    # else keep recursing down the big tree
    return sub_tree(t1.left, t2) or sub_tree(t1.right, t2)

def match_tree(t1, t2):
    if t1 is None and t2 is None:
        # nothing left in the subtree
        return True
    elif t1 is None or t2 is None:
        # exactly one tree is empty so trees don't match
        return False
    elif t1.data != t2.data:
        # found nodes that don't match so trees don't match
        return False
    else:
        return match_tree(t1.left, t2.left) and match_tree(t1.right, t2.right)

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def check_parents(self):
        if self.left:
            self.left.check_parents()
        if self.parent is None:
            print(f"the parent of {self.data} is: {self.parent}")
        else:
            print(f"the parent of {self.data} is: {self.parent.data}")
        if self.right:
            self.right.check_parents()

    def insert(self, new_data):
        # inserts a node with a link to its parent
        if self.data is None:
            self.data = new_data
        else:
            if new_data <= self.data:
                if self.left is not None:
                    temp = self.left.insert(new_data)
                    self.left = temp
                    temp.parent = self 
                else:
                    # left is node so let's insert it
                    temp = Node(new_data)
                    self.left = temp
                    temp.parent = self
            else:
                if self.right is not None:
                    temp = self.right.insert(new_data)
                    self.right = temp
                    temp.parent = self 
                else:
                    # right is node so let's insert it
                    temp = Node(new_data)
                    self.right = temp
                    temp.parent = self
            return self


root1 = Node(5)
root1.insert(2)
root1.insert(8)
root1.insert(1)
root1.insert(3)
root1.insert(6)
root1.insert(9)  

root2 = Node(2)
root2.insert(1)
root2.insert(3)  

root3 = Node(2)
root3.insert(1)
root3.insert(4) 

root4 = Node(8)
root4.insert(9)
root4.insert(10)

root5 = Node(9)


class TestTree(unittest.TestCase):
    def test_case1(self):
        self.assertTrue(check_subtree(root1, root2))
    
    def test_case2(self):
        self.assertFalse(check_subtree(root1, root3))

    def test_case3(self):
        self.assertFalse(check_subtree(root1, root4))

    def test_case4(self):
        self.assertTrue(check_subtree(root1, root5))
     
unittest.main(verbosity=2)
# print(check_subtree(root1, root2))