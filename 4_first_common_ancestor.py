'''
First Common Ancestor: Design an algorithm and write code to find 
the first common ancestor of two nodes in a binary tree. Avoid 
storing additional nodes in a data structure. 
NOTE: This is not necessarily a binary search tree.

pg 121
sol: 268
'''

'''
finds the common ancestor in a tree without links to parents
'''
def find_common_ancestor_no_parent(root, p, q):
    # let's check if one of the nodes is not in the tree
    if not covers(root, p) or not covers(root, q):
        return None
    return ancestor_helper(root, p, q)

def ancestor_helper(root, p, q):
    if root is None or root == p or root == q:
        return root

    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)
    # check if nodes diverged to different sides of tree
    if p_is_on_left != q_is_on_left:
        return root

    child_side = p_is_on_left = root.left if p_is_on_left is True else root.right
    
    return ancestor_helper(child_side, p , q)

def covers(root, node):
    if root is None: return False
    if root == node: return True
    return covers(root.left, node) or covers(root.right, node)



'''
finds the common ancestor between two nodes in a tree that has
nodes with parent links
'''
def find_common_ancestor_with_parent(root, p, q):
    # check for one of the nodes not on the tree and
    # check if one contains the other
    if (subtree_contains_node(root, p) is False or
        subtree_contains_node(root, q) is False):
        return None
    elif subtree_contains_node(p,q):
        return p
    elif subtree_contains_node(q,p):
        return q

    # traverse the tree up until a node subtree that contains q is found
    sibling = get_sibling_subtree(p)
    parent = p.parent

    while not subtree_contains_node(sibling, q):
        sibling = get_sibling_subtree(parent)
        parent = parent.parent
    return parent

def subtree_contains_node(root, node):
    if root is None: return False
    if root == node: return True
    res = subtree_contains_node(root.left, node) or \
        subtree_contains_node(root.right, node)
    return res

def get_sibling_subtree(node):
    if node is None or node.parent is None:
        return None
    parent = node.parent
    if parent.left == node:
        return parent.right
    else:
        return parent.left

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value)
        if self.right:
            self.right.PrintTree()

    def check_parents(self):
        if self.left:
            self.left.check_parents()
        if self.parent is None:
            print(f"the parent of {self.value} is: {self.parent}")
        else:
            print(f"the parent of {self.value} is: {self.parent.value}")
        if self.right:
            self.right.check_parents()

    def insert(self, new_value):
        # inserts a node with a link to its parent
        if self.value is None:
            self.value = new_value
        else:
            if new_value <= self.value:
                if self.left is not None:
                    temp = self.left.insert(new_value)
                    self.left = temp
                    temp.parent = self 
                else:
                    # left is node so let's insert it
                    temp = Node(new_value)
                    self.left = temp
                    temp.parent = self
            else:
                if self.right is not None:
                    temp = self.right.insert(new_value)
                    self.right = temp
                    temp.parent = self 
                else:
                    # right is node so let's insert it
                    temp = Node(new_value)
                    self.right = temp
                    temp.parent = self
            return self


root = Node(5)
root.insert(2)
root.insert(8)
root.insert(1)
root.insert(3)
root.insert(6)
root.insert(9)  

#checking parent links are valid
# root.check_parents()

# print("Inorder traversal of tree: ")
# root.PrintTree()

node2 = root.left
node3 = root.left.right
node8 = root.right
node6 = root.right.left

# print("with no parents: ", find_common_ancestor_no_parent(root, node3, node8).value)
print("with parents: ", find_common_ancestor_with_parent(root, node3, node8).value)

