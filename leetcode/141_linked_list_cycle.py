'''
Given head, the head of a linked list, determine if the linked list 
has a cycle in it.

There is a cycle in a linked list if there is some node in the 
list that can be reached again by continuously following the next 
pointer. Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. Note that pos is not 
passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, 
return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail 
connects to the 1st node (0-indexed).
'''


def has_cycle(head):
    # use Floyd's Tortoise and Hare algorithm
    slow = head
    fast = head

    while fast is not None and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False



'''
The solution below, although it works, it uses O(n) time and space complexity
this problem can be solved with O(1) space
'''
def has_cycle2(head):
    seen_nodes = set()
    curr = head
    while curr is not None:
        if curr in seen_nodes:
            return True
        else:
            seen_nodes.add(curr)
            curr = curr.next
    return False