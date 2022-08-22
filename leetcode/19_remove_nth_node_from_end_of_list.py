'''
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
'''

def remove_nth_node(head, n):
    '''
    this algo adds a dummy node at the start of the list so that
    we can leverage it for an easier removal in one pass of the list.
    '''
    dummy = ListNode(0,head)
    right = head

    while n > 0 and right is not None:
        right = right.next
        n -= 1

    left = dummy
    
    while right is not None:
        right = right.next
        left = left.next

    left.next = left.next.next
    return dummy.next

    