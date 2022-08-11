'''
Successor: Write an algorithm to find the "next" node (i.e., in-order successor, as in the node that comes after the given node) of a given node in a
binary search tree. You may assume that each node has a link to its parent
'''

# binary tree node
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        if self.right:
            self.right.PrintTree()
        print(self.value)


def inorder_sucessor(node):
    if node is None:
        return None

    if node.right is not None:
        return leftmost_child_of_subtree(node.right)
    p = node.parent
    while( p is not None):
        if node != p.right :
            break
        node = p
        p = p.parent
    return p
   


# get the min node from current binary subtree
def leftmost_child_of_subtree(node):
    if node is None:
        return None
    while node.left is not None:
        node = node.left
    return node
  

def insert(node, new_value):
    if node is None:
        return Node(new_value)
    else:
        if new_value <= node.value:
            temp = insert(node.left, new_value)
            node.left = temp
            temp.parent = node 
        else:
            temp = insert(node.right, new_value)
            node.right = temp
            temp.parent = node
        return node

root = Node(5)
insert(root, 2)
insert(root, 8)
insert(root, 1)
insert(root, 3)
insert(root, 6)
insert(root, 9)  

print("Inorder traversal of tree: ")
root.PrintTree()
node2 = root.left
node3 = root.left.right
node8 = root.right
node6 = root.right.left
node9 = root.right.right # doesn't exist

print("inorder_sucessor should be 6 got: ", inorder_sucessor(root).value)
print("inorder_sucessor should be 3 got: ", inorder_sucessor(node2).value)
print("inorder_sucessor should be 5 got: ", inorder_sucessor(node3).value)
print("inorder_sucessor should be 8 got: ", inorder_sucessor(node6).value)
# print("inorder_sucessor should raise exception. got: ", inorder_sucessor(node9).value)

