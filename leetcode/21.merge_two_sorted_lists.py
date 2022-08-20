'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''


def merge_lists(list1, list2):
        h1 = list1
        h2 = list2
        merged = None
        merged_last = None

        # stablish the new head
        if h1 is not None and h2 is not None:
            if h1.val < h2.val:
                merged = h1
                merged_last = merged
                h1 = h1.next
            else:
                merged = h2
                merged_last = merged
                h2 = h2.next

        while h1 is not None or h2 is not None:
            if h1 is None:
                if merged is None:
                    merged = h2
                else:
                    merged_last.next = h2
                return merged
            elif h2 is None:
                if merged is None:
                    merged = h1
                else:
                    merged_last.next = h1
                return merged
            else:
                if h1.val <= h2.val:
                    merged_last.next = h1
                    h1 = h1.next
                elif h1.val > h2.val:
                    merged_last.next = h2
                    h2 = h2.next
                merged_last = merged_last.next

        return merged