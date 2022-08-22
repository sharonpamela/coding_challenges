'''
You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted 
linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
'''

def merge_lists(lists):
    if len(lists) == 0 or len(lists[0]):
        return None
    if len(lists) == 1:
        return lists[0]
    
    main = lists.pop()

    while len(lists) > 0:
        second_list =  lists.pop()
        main = merge_two_lists(main, second_list)

    return main

def merge_two_lists(l1, l2):

    dummy = ListNode()
    last = dummy
    while list1 and list2:
        if list1.val < list2.val:
            last.next = list1
            list1 = list1.next
        else:
            last.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1 is None:
        last.next = list2
    else:
        last.next = list1
    
    return dummy.next