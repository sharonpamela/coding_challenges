'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
'''

def find_min1(nums):
    l, r = 0, len(nums)-1
    res = nums[0]
    
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res,nums[l])
            break
        mid = (r + l) // 2
        res = min(res, nums[mid])
        if nums[l] <= nums[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return res

def find_min(nums):
    if len(nums) == 1:
        return nums[0]

    l, r = 0, len(nums)-1
    
    while l < r:
        mid = (r + l) // 2
        
        if nums[mid] >= nums[l]:
            # we must go to the right
            l = mid
        else:
            # we must go to the left
            r = mid
        
        if nums[l + 1] == nums[r]:
            # There are no numbers between l and r
            # check if there is no pivot
            if nums[len(nums)-1] > nums[0]:
                return nums[0]
            else:
                return nums[l + 1]


n = [3,4,5,1,2]
# n = [11,13,15,17]
# n = [4,3]
# n = [1]
# n = [1,2]
n = [3,1,2]
print(find_min1(n))   
        