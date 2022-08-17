'''
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4

Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
'''

def longest_consecutive_seq(nums):
    max_seq_seen = 0
    n_set = set(nums)

    for num in n_set:
        if num-1 not in n_set:
            # this is the start of a sequence
            streak = 0
            while num+streak in n_set:
                streak += 1
            max_seq_seen = max(max_seq_seen, streak)
            
    return max_seq_seen

nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [1,2,0,1]
print("res: ", longest_consecutive_seq(nums))