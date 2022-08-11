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
        # result.append(LinkedList()) # append empty list
        return result
    
    prefix = LinkedList()
    prefix.append(node.data)

    # recurse on left and right subtrees
    left_seq = get_sequences(node.left) # [ [] [] ] both empty
    right_seq = get_sequences(node.right) # [ [] [] ] both empty

    # print(f"left seq:  {left_seq}")
    # print(f"right seq: {right_seq}")
    
    # if both left and right lists are empty, then we are visiting a leaf node
    # add the leave to the results array to weave later with possible other leaf 
    # at current level
    if len(left_seq) == 0 and len(right_seq) == 0:
        leaf_linkedList = LinkedList()
        leaf_linkedList.append(node.data)
        # print(f"leaf_linkedList {leaf_linkedList}")
        result.append(leaf_linkedList)
        # print(f"result after linked list appended: {result}")

    # weave together each list from the left and the right
    for l_linkedlist in left_seq:
        for r_linkedlist in right_seq:
            weaved = []
            # print(f"weave_lists({l_linkedlist}, {r_linkedlist}, {weaved}, {prefix})")
            # print(f"l.size {l_linkedlist.size} == 0 or r.size {r_linkedlist.size} == 0")
            weave_lists(l_linkedlist, r_linkedlist, weaved, prefix)
            # print(f" add_all_weaved(result:{result}, and weived: {weaved})")
            add_all_weaved(result, weaved)
    return result

def add_all_weaved(l1, l2):
    for item in l2:
        l1.append(item)

def add_all(result, ll):
    # result is an array list
    # ll is a linked list
    curr_node = ll.head
    while curr_node is not None:
        result.append(curr_node)
        curr_node = curr_node.next

def weave_lists(first_linkedlist, second_linkedlist, weaved, prefix):
    # if one list is empty, add reminder to [cloned]
    # prefix and store result
    # print(f"first.size {first_linkedlist.size == 0} or second.size {second_linkedlist.size == 0}")
    if first_linkedlist.size == 0 or second_linkedlist.size == 0:
        result = weaved.copy() # weaved is an array of linkedlists
        add_all(result, first_linkedlist)
        add_all(result, second_linkedlist)
        # print(f"result after adding first or second {result[0]}")
        # print(result[0])
        weaved.append(result)
        # print(f"weaved after adding result: {weaved[0]}")
        return

    # recurse with head of first linkedlist added to the prefix
    # removing the head will alter first, so need to
    # put the head back in orig place afterwards
    head_first = first_linkedlist.remove_first()
    prefix.append(head_first)
    weave_lists(first_linkedlist, second_linkedlist, weaved, prefix)
    prefix.remove_last()
    first_linkedlist.append_first(head_first)

    # same thing as above but this time with second linkedlist
    head_second = second_linkedlist.remove_first()
    prefix.append(head_second)
    weave_lists(first_linkedlist, second_linkedlist, weaved, prefix)
    prefix.remove_last()
    second_linkedlist.append_first(head_second)


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, node):
        # appends to the end of the list
        if self.head is None:
            self.head = LinkedListNode(node)
            self.last = self.head
        else:
            temp = LinkedListNode(node)
            self.last.next = temp
            self.last = temp
        self.size += 1

    def append_first(self, node):
        # adds a node as the new head of list
        temp = LinkedListNode(node)
        temp.next = self.head
        self.head = temp
        self.size += 1
        
    def add_all(self, list_to_add):
        # adds all nodes from list_to_add to current linked list
        if list_to_add is not None:
            if self.head is None:
                self.head = list_to_add.head
                self.last = list_to_add.last
            else:
                print(f"self head: {self.head.data} self last: {self.last}")
                self.last.next = list_to_add.head
                self.last = list_to_add.last
                self.size += list_to_add.size

    def remove(self, node):

        curr_node = self.head
        # if the node to remove is the head
        if curr_node.data == node:
            # reset last if list only has one elem
            if self.head.next is None:
                self.last = None
            self.head = self.head.next
            return curr_node
        
        # else the node to remove is not the head
        prev = curr_node
        while curr_node is not None:
            if curr_node.data == node:
                prev.next = curr_node.next
                self.size -= 1
                # returned the removed node
                return curr_node
            prev = curr_node
            curr_node = curr_node.next
        # returns None if the node to be removed is not found
        return None
        
    def remove_last(self):
        curr_node = self.head
        prev = curr_node
        if self.head is None: return None
        if self.head == self.last:
            last = self.last
            self.head = None
            self.last = None
            return last

        while curr_node.next is not None:
            prev = curr_node
            curr_node = curr_node.next
        prev.next = curr_node.next
        self.last = prev
        self.size -= 1
        return curr_node

    def remove_first(self):
        # removes the head of the list
        curr_node = self.head
        
        # reset last if list only has one elem
        if self.head.next is None:
            self.last = None
        # the new head is none if head was the only
        # elem in the list or the next elem prev head
        # was pointing to
        self.head = self.head.next
        self.size -= 1
        return curr_node

    def copy_list(self):
        # Function takes a linked list and returns its complete copy
        current = self.head      # used to iterate over the original list
        # print(f"current head {self.head}")
        new_list = LinkedList()  # new list
    
        while current is not None:
            new_list.append(current.data)
            current = current.next
        print(f"New list copied {new_list}")
        return new_list

class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

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
root = TreeNode(2)
root.insert(1)
root.insert(3)

# test get_sequences
print(f"all sequences: {get_sequences(root)}")


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



# root = TreeNode(5)
# root.insert(3)
# root.insert(8)
# root.insert(2)
# root.insert(4)
# root.insert(6)
# root.insert(10)

# print("Inorder traversal of tree: ")
# root.PrintTree()

# test getsecuences
# print(get_sequences(root))