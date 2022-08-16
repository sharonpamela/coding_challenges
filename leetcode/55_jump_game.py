'''
You are given an integer array nums. 
You are initially positioned at the array's 
first index, and each element in the array 
represents your maximum jump length at that position.
Return true if you can reach the last index, 
or false otherwise.

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
'''

# backtracking aproach
# def canJump(nums):
#     return canJumpFromPosition(0, nums)
    
# def canJumpFromPosition(position, nums):

#     if position == len(nums) - 1:
#         return True
    
#     furthest_jump = min(position + nums[position], len(nums) - 1)
#     for next_position in range(position + 1, furthest_jump + 1):
#         if canJumpFromPosition(next_position, nums):
#             return True
#     return False



# dynamic programming topdown approach
# class Solution():
#     def __init__(self):
#         self.memo = []

#     def canJump(self, nums):
#         self.memo = ['unknown'] * len(nums)
#         for i in range(len(nums)-1):
#             self.memo[i] = 'unknown'
#         self.memo[len(nums)-1] = 'good'
#         return self.canJumpFromPosition(0, nums)

#     def canJumpFromPosition(self, position, nums):
#         if self.memo[position] != 'unknown':
#             return True if self.memo[position] == "good" else False

#         furthest_jump = min(position + nums[position], len(nums)-1)
#         for next_position in range(furthest_jump, position, -1):
#             if self.canJumpFromPosition(next_position, nums):
#                 self.memo[position] =  "good"
#                 return True
#         self.memo[position] = "bad"
#         return False 



# dynamic programming bottom up aproach


class Solution():
    def __init__(self):
        self.memo = []

    def canJump(self, nums):
        self.memo = ['unknown'] * len(nums)
        for i in range(len(nums)-1):
            self.memo[i] = 'unknown'
        
        # the last position is always good
        self.memo[len(nums)-1] = 'good'

        # starting at index to the left of last value
        # stopping at 0
        # decreasing by 1
        for i in range(len(nums)-2, -1, -1):
            is_good_idx = self.is_good_index(i, i+nums[i])
            if is_good_idx:
                self.memo[i] = "good"
            else:
                 self.memo[i] = "bad"

        return self.memo[0] == "good"

    def is_good_index(self, starting_index, end_index):
        # checks if there is a "good" index within the curr starting
        # index's jump range
        for i in range(starting_index, end_index+1):
            if self.memo[i] == "good":
                return True
        return False
         
res = Solution()
print(res.canJump([3,2,1,1,4])) # true
print(res.canJump([3,2,1,0,4])) # false
print(res.canJump([2,0])) # true