'''
Random Node: You are implementing a binary tree class from scratch which, 
in addition to insert, find, and delete, has a method getRandomNode() 
which returns a random node from the tree. All nodes should be equally 
likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the 
methods. 
'''
from random import randint
 
class Node:
     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.children = 0
 
# This is used to fill children counts.
def getElements(root):
 
    if root == None:
        return 0
         
    return (getElements(root.left) +
            getElements(root.right) + 1)
 
# Inserts Children count for each node
def insertChildrenCount(root):
 
    if root == None:
        return
 
    root.children = getElements(root) - 1
    insertChildrenCount(root.left)
    insertChildrenCount(root.right)
 
# Returns number of children for root
def children(root):
 
    if root == None:
        return 0
    return root.children + 1
 
# Helper Function to return a random node
def randomNodeUtil(root, count):
 
    if root == None:
        return 0
 
    if count == children(root.left):
        return root.data
 
    if count < children(root.left):
        return randomNodeUtil(root.left, count)
 
    return randomNodeUtil(root.right,
            count - children(root.left) - 1)
 
# Returns Random node
def randomNode(root):
 
    count = randint(0, root.children)
    return randomNodeUtil(root, count)
 

 
# Creating sample Tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.right = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

insertChildrenCount(root)

print("A Random Node From Tree :",randomNode(root))

# from random import randrange

# class TreeNode(object):
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.size = 1

    
#     def get_random_node(self):
#         left_size = 0 if self.left == None else self.left.size()
#         index = randrange(self.size) # between 0-size inclusive
        
#         if index < left_size:
#             return self.left.get_random_node()
#         elif index == left_size:
#             return self
#         else:
#             return self.right.get_random_node()
    
#     def insert_in_order(self, data):
#         if data <= self.data:
#             if self.left is None:
#                 self.left = TreeNode(data)
#             else:
#                 self.left.insert_in_order(data)
#         else:
#             if self.right is None:
#                 self.right = TreeNode(data)
#             else:
#                 self.right.insert_in_order(data)
        
#         self.size += 1

    
#     def find(self, d):
#         if d == self.data:
#             return self
#         elif d <= self.data:
#             return self.left.find(d) if self.left is not None else None
#         elif d > self.data:
#             return self.right.find(d) if self.right is not None else None
#         return None