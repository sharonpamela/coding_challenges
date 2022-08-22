'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [1], target = 0
Output: -1
'''


def find_elem(nums, target):
    
    l,r = 0, len(nums)-1

    while l <= r:
        mid_idx = (r+l) // 2
        mid_val = nums[mid_idx]

        if target == mid_val:
            return mid_idx

        if nums[l] <= mid_val:
            # we are on the left sorted side of array
            if target > mid_val or target < nums[l]:
                # we sort the right most portion
                l = mid_idx + 1
            else:
                # target < mid and target > left
                # we sort the left right portion
                r = mid_idx - 1
        else:
            # we are on the right sorted side of array
            if target < mid_val or target > nums[r]:
                r = mid_idx - 1
            else:
                # target is > mid and target < rightmost
                l = mid_idx + 1

    return -1

print(find_elem([4,5,6,7,0,1,2], 3))

