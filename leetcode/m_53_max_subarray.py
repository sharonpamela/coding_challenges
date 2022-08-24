'''
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''



'''
the solution below performs in linear time
'''
def find_max_sub_array(nums):
    current_sum = 0
    max_sum = nums[0]
    for num in nums:
        if current_sum < 0:
            current_sum = 0
        current_sum += num
        max_sum = max(max_sum, current_sum)          
    return max_sum



'''
the solution below performs in quadratic time.
'''
def find_max_sub_array2(nums):
    current_sum = 0
    max_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
        current_sum = 0
    return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(find_max_sub_array(nums))


