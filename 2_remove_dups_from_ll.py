'''
Remove Dups! Write code to remove duplicates from an unsorted linked list. 
'''

def remove_dups(linked_list):
    seen_elems = set()
    curr_node = prev = linked_list.head
    while curr_node:
        if curr_node.data in seen_elems:
            # this is a dup, remove it
            prev.next = curr_node.next
            curr_node = prev
        seen_elems.add(curr_node.data)
        prev = curr_node
        curr_node = curr_node.next
   
'''
remove_dups has O(n) time complexity bc it has to walk thru entire LL worse case.
space complexity is o(n) bc auxiliary set may grow to n elems worse case.
'''
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
print(llist1)
print("Removing duplicates...")
remove_dups(llist1)
print(llist1)

# Test two:
llist = LinkedList()
first_node = Node("d")
llist.head = first_node
second_node = Node("d")
third_node = Node("d")
fourth_node = Node('d')
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
print(llist)
print("Removing duplicates...")
remove_dups(llist)
print(llist)