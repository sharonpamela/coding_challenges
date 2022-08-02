'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f 
'''

def delete_middle_node(middle_node):
    '''
    deletes a node in a LL but doesn't work for last node
    '''
    next_node = middle_node.next
    
    if next_node is not None:
        middle_node.data = next_node.data
        middle_node.next = next_node.next
        return True
    else:
        return False

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
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

# Test one:
llist1 = LinkedList()
first_node = Node("g")
llist1.head = first_node
second_node = Node("b")
third_node = Node("b")
fourth_node = Node('u')
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

print("deleting second node...")
delete_middle_node(second_node)
print(llist1)
