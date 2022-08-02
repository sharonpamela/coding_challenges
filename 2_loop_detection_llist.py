'''
Loop Detection: Given a circular linked list, implement an algorithm 
that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next 
pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C 
'''

def find_loop(l1):
    seen = set()
    node = l1.head

    while node is not None:
        if node.data not in seen:
            seen.add(node.data)
        else:
            return node
        node = node.next

            

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# Test one:
l1 = LinkedList()
first_node = Node('a')
l1.head = first_node
second_node = Node('b')
third_node = Node('c')
fourth_node = Node('d')
fith_node = Node('e')
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fith_node
fith_node.next = third_node

print(find_loop(l1)) # true
