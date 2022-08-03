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

'''
The solution below is O(1) for space and O(n)
'''
def find_loop(l1):
    slow = l1.head
    fast = l1.head

    # step 1: Find meeting point. This will be LOOP_SIZE - k steps into the linked list.
    while slow != None or fast != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # step 1.1: if there is no meeting point from prev step, there is no cycle/loop
    if slow == None or fast == None:
        return False

    # step 2: Move slow to Head. Keep fast at Meeting Point. 
    # Each are k steps from the Loop Start. If they move at 
    # the same pace, they must meet again  at Loop Start
    slow = l1.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast



'''
the solution below finds the begining of the loop, 
however, it depends on the value of the node. which means
the link list could not have any other duplicate values anywhere.
this solution alse depends on an additional data structure to
keep track of the seen values. this makes it O(n) for space and 
time complexities. there are better approaches to this such as the 
one above.
'''

# def find_loop(l1):
#     seen = set()
#     node = l1.head

#     while node is not None:
#         if node.data not in seen:
#             seen.add(node.data)
#         else:
#             return node
#         node = node.next

            

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
third_node = Node('c') #<-- start of loop
fourth_node = Node('d')
fith_node = Node('e')
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node
fourth_node.next = fith_node
fith_node.next = third_node #<-- loop created

print(find_loop(l1)) # c
