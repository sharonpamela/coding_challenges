'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input:
Output:
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

def partition(node, partition):

    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while node is not None:
        next_node = node.next
        node.next = None
        if node.data < partition:
            if before_start is None:
                before_start = node
                before_end = before_start
            else:
                before_end.next = node
                before_end = node
        else:
            if after_start is None:
                after_start = node
                after_end = after_start
            else:
                after_end.next = node
                after_end = node
        node = next_node

    if before_start is None:
        return after_start
    
    before_end.next = after_start
    return before_start
        
    
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
llist1 = LinkedList()
first_node = Node(3)
llist1.head = first_node
second_node = Node(5)
third_node = Node(8)
fourth_node = Node(5)
fith_node = Node(10)
sith_node = Node(2)
seventh = Node(1)
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fith_node
fith_node.next = sith_node
sith_node.next = seventh

part=5
print(f"Partitioning linked list {llist1} given elem: {part}...")
partition(first_node, part)
print(llist1)
