'''
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists). 
'''

from collections import deque

def create_lists_of_depths(root):

    q = deque()
    q.append((root,1))
    start_level = 1
    level_lists = {}

    while len(q) > 0:
        curr_node, node_level = q.popleft()
        
        if node_level in level_lists:
            # grab the linked list 
            curr_linked_list = level_lists[node_level]
            # create a new node to be added to LL
            new_node = LinkedListNode(curr_node.value)
            # add the new node to the end of the linkedList
            curr_linked_list.last.next = new_node
            # adjust new last node of LL 
            curr_linked_list.last = new_node
        else:
            # create the first node of LL:
            first_node = LinkedListNode(curr_node.value)
            # create a new linked list and store its head node under the corresponding level
            level_lists[node_level] = LinkedList(first_node)
        
        if node_level > start_level:
            start_level+=1
        
        if curr_node.left:
            q.append((curr_node.left, start_level+1))
        if curr_node.right:
            q.append((curr_node.right, start_level+1))
    
    # optional print all levels to visualize results
    for level in level_lists:
        print(f"Level {level}: {level_lists[level]}")


class LinkedList(object):
    def __init__(self, head_node):
        self.head = head_node
        self.last = head_node
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

class LinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

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
                if new_value < self.value:
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
# root.PrintTree()

create_lists_of_depths(root)