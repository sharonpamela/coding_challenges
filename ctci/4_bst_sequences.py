'''
BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.
EXAMPLE
Input:
Output: {2, 1, 3}, {2, 3, 1} 
'''
from collections import deque

def get_sequences(node):
    result = []

    if node is None:
        return result
    
    prefix = deque()
    prefix.append(node.data)

    # recurse on left and right subtrees
    left_seq = get_sequences(node.left)
    right_seq = get_sequences(node.right)

    # if both left and right lists are empty, then we are visiting a leaf node
    # add the leave to the results array to weave later with possible other leaf 
    # at current level
    if len(left_seq) == 0 and len(right_seq) == 0:
        leaf = deque()
        leaf.append(node.data)
        result.append(leaf)

    # weave together each list from the left and the right
    for l in left_seq:
        for r in right_seq:
            weaved = deque()
            weave_lists(l, r, weaved, prefix)
            result += weaved
    return result


def weave_lists(first, second, weaved, prefix):
    # if one list is empty, add reminder to [cloned]
    # prefix and store result
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy() 
        result += first 
        result += second
        weaved.append(result)
        # print(f"appended prefix results to weaved: {weaved}")
        return

    # recurse with head of first list added to the prefix
    # removing the head will alter first, so need to
    # put the head back in orig place afterwards
    # print(f"starting first list weave first: {first}, second: {second}, weaved: {weaved} prefix: {prefix}")
    head_first = first.popleft()
    prefix.append(head_first)
    # print(f"Recursing first list weave first: {first}, second: {second}, weaved: {weaved} prefix: {prefix}")
    weave_lists(first, second, weaved, prefix)
    prefix.pop()
    first.appendleft(head_first)

    # print(f"starting second list weave first: {first}, second: {second}, weaved: {weaved} prefix: {prefix}")
    # same thing as above but this time with second linkedlist
    head_second = second.popleft()
    prefix.append(head_second)
    # print(f"Recursing second list weave first: {first}, second: {second}, weaved: {weaved} prefix: {prefix}")
    weave_lists(first, second, weaved, prefix)
    prefix.pop()
    second.appendleft(head_second)

class TreeNode(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, new_data):
            if self.data:
                if new_data < self.data:
                    if self.left is None:
                        self.left = TreeNode(new_data)
                    else:
                        self.left.insert(new_data)
                elif new_data > self.data:
                    if self.right is None:
                        self.right = TreeNode(new_data)
                    else:
                        self.right.insert(new_data)
            else:
                self.data = new_data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()


# create sample tree to test with
# root = TreeNode(2)
# root.insert(1)
# root.insert(3)

# test linkedList
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# print(ll.remove(2).data)
# print(ll.remove(1).data)
# print(ll.remove(3).data)
# ll.append(7)
# print(ll)


# testing tree # 2
root = TreeNode(5)
root.insert(3)
root.insert(8)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(10)

# print("Inorder traversal of tree: ")
# root.PrintTree()

print("Answer", get_sequences(root))