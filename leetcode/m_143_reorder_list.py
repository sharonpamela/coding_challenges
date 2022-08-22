'''
You are given the head of a singly linked-list.  
The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    # find the middle of the list
    s = head
    f = head.next
    while f and f.next:
        s = s.next
        f = f.next.next

    # divide the list into first and second parts
    curr_first_list_node = head
    second_list_node = s.next
    s.next = None # finish list break up by pointing first list to Null

    # reverse second linkedlist
    curr = second_list_node
    prev = None
    next_node = None
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    curr_second_list_node = prev

    # merge the first and second lists, starting with the first
    while curr_second_list_node is not None:
        temp1, temp2 = curr_first_list_node.next, curr_second_list_node.next
        curr_first_list_node.next = curr_second_list_node
        curr_second_list_node.next = temp1
        curr_first_list_node = temp1
        curr_second_list_node = temp2

