'''
Validate BST: Implement a function to check if a binary tree is a binary search tree. 
'''

def validate_bst(node):

    max_bound = float('inf')
    min_bound = float('-inf')

    return traverse_with_bounds(node, max_bound, min_bound)


def traverse_with_bounds(node, max_bound, min_bound):

    if node.value > max_bound or node.value < min_bound:
        return False

    if node.left is not None:
        new_max = node.value
        traverse_with_bounds(node.left, new_max, min_bound)
    if node.right is not None:
        new_min = node.value
        traverse_with_bounds(node.right, max_bound, new_min)
    
    return True

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value is not None:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            
            else:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def __repr__(self):
        if self.right is not None:
            fmt = '{}({value!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({value!r}, {left!r})'
        else:
            fmt = '{}({value!r})'
        return fmt.format(type(self).__name__, **vars(self))

root = Node(5)
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
# root.PrintTree()
# print(root)

print(validate_bst(root))