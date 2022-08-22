'''
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

'''

def reverse_linked_list(node):

    curr_node = node
    prev = None
    next = None

    while curr_node is not None:
        next = curr_node.next
        curr_node.next = prev
        prev = curr_node
        curr_node = next
    return prev