'''
Given an integer array nums and an integer k, return the 
k most frequent elements. 
You may return the answer in any order.

We know k is within bounds of nums array

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''
from collections import Counter
from queue import Empty

def top_elems(nums, k):
    
    counts = Counter(nums)

    return [(k) for (k,v) in sorted(counts.items(), key=lambda x:x[1], reverse=True)][:k]


def top_elems2(nums, k):

    bucket_sort = [[] for n in range(len(nums)+1)]
    res = []

    # create count with all items
    counts =  {}
    for num in nums:
        counts[num] = 1 + counts.get(num,0)

    # sort all counts into buckets[count] = item
    # where the index placement inside the buckets list == count
    for n,c in counts.items():
        if c != 0:
            bucket_sort[c].append(n) 
    
    # return the last k elems, which by default would be the greatest counts
    for i in range(len(bucket_sort)-1, 0, -1):
        for elem in bucket_sort[i]:
            res.append(elem)
            if len(res) == k:
                return res



nums = [1,1,1,2,2,3]
nums = [5,5,5,6,6,8]
k = 2
print(top_elems2(nums, k))