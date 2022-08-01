'''
 Return Kth to Last: Implement an algorithm to find the kth to 
 last element of a singly linked list. 
'''

def k_to_last(linked_list, k):
    last_node = k_node = linked_list.head

    # advance the last node k spaces forward
    for _ in range(k):
        if last_node is not None:
            print("Last node", last_node.data)
            last_node = last_node.next
        else:
            raise Exception("K is too large for LL")
 
    # advance both until last_node reached end of LL
    while last_node is not None and last_node.next is not None:
        last_node = last_node.next
        k_node = k_node.next
    return k_node.data
    

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

print("Finding k to last node...")
k=0
print(k_to_last(llist1, k))

