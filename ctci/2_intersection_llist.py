'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
Return the intersecting node. Note that the intersection is defined based on reference, 
not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node 
of the second linked list, then they are intersecting.
'''

def find_intercept(ll1,ll2):
    
    l1 = ll1.head
    l2 = ll2.head

    # 1. Run through each linked list to get the lengths and the tails.
    ll1_len = ll2_len = 0
    ll1_tail = ll2_tail = None
    
    while l1 is not None:
        ll1_len+=1
        ll1_tail = l1
        l1 = l1.next

    while l2 is not None:
        ll2_len+=1
        ll2_tail = l2
        l2 = l2.next

    # 2. Compare the tails. If they are different (by reference, not by value), 
    # return immediately. There is no intersection.
    if ll1_tail != ll2_tail:
        return False

    # 3. Set two pointers to the start of each linked list.
    ll1_start = ll1.head
    ll2_start = ll2.head

    # 4. On the longer linked list, advance its pointer by the difference in lengths.
    diff = abs(ll1_len - ll2_len)
    if ll1_len > ll2_len:
        while diff != 0:
            ll1_start = ll1_start.next
            diff -= 1
    else:
        while diff != 0:
            ll2_start = ll2_start.next
            diff -= 1

    # 5. Now, traverse on each linked list until the pointers are the same
    while ll1_start != ll2_start:
        ll1_start = ll1_start.next
        ll2_start = ll2_start.next

    return ll1_start

         

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
first_node1 = Node('a')
l1.head = first_node1
second_node1 = Node('b')
third_node1 = Node('c')
fourth_node1 = Node('d')
fith_node1 = Node('e')
first_node1.next = second_node1
second_node1.next = third_node1
third_node1.next = fourth_node1
fourth_node1.next = fith_node1


l2 = LinkedList()
first_node = Node('z')
l2.head = first_node
second_node = Node('y')
third_node = Node('x')
first_node.next = second_node
second_node.next = third_node
third_node.next = third_node1

#                *
#      a -> b -> c -> d -> e -> None
# z -> y -> x -> c -> d -> e -> None (same s,d,e nodes as above llist)
print(find_intercept(l1, l2).data) # c