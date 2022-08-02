'''
Palindrome: Implement a function to check if a linked list is a palindrome. 
'''

'''
this solution for is_palindrome is O(n) time and O(n) space as it passes thru all nodes 
in the linked list, however, the additional stack used to compare the elements only 
holds n/2 elements max
'''
def is_palindrome(llist):
    fast = llist.head
    slow = llist.head

    seen = []

    while fast is not None and fast.next is not None:
        seen.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    # if odd word, skip middle char
    if fast is None:
        slow = slow.next

    while slow is not None:
        if seen.pop() != slow.data:
            return False
        slow = slow.next

    return True


'''
is_palindrome2 is O(n) time and space complexity. we can do better by using the link
list to perform our comparisons directly without the additional set.
'''
def is_palindrome2(llist):

    seen = set()

    node = llist.head

    while node is not None:
        if node.data not in seen:
            seen.add(node.data)
        else:
            seen.remove(node.data)
        node = node.next

    return len(seen) <=1


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
third_node = Node('a')
first_node.next = second_node
second_node.next = third_node


l2 = LinkedList()
first_node = Node('a')
l2.head = first_node
second_node = Node('b')
third_node = Node('a')
fourth_node = Node('a')
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

print(is_palindrome(l1)) # true
print(is_palindrome(l2)) # false
