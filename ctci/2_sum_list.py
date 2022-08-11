'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 -> 1 -> 2. That is, 912. 
'''

def sum_list(llist1, llist2):
    carry = 0
    result = LinkedList()

    l1 = llist1.head
    l2 = llist2.head

    while l1 is not None or l2 is not None:

        n1 = l1.data if l1.data is not None else 0
        n2 = l2.data if l2.data is not None else 0

        sum = n1 + n2 + carry
        res = sum % 10
        carry = 1 if res > 0 else 0

        # append result to result llist
        if result.head is None:
            result.head = Node(res)
            # print(str(result.head.data))
        else:
            old_head = result.head
            new_head = Node(res)
            new_head.next = old_head
            result.head = new_head
            # print(str(result.head.data))

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
            
    return result


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
first_node = Node(7)
l1.head = first_node
second_node = Node(1)
third_node = Node(6)
first_node.next = second_node
second_node.next = third_node

l2 = LinkedList()
fourth_node = Node(5)
l2.head =  fourth_node
fith_node = Node(9)
sixth_node = Node(2)
fourth_node.next = fith_node
fith_node.next = sixth_node


print(f"Adding two nums...")
print(sum_list(l1,l2))
