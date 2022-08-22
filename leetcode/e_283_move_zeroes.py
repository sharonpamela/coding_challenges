'''
Given an integer array nums, move all 0's to the end 
of it while maintaining the relative order of the 
non-zero elements.

Note that you must do this in-place without making a 
copy of the array
'''

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    lastModified = 0
    # copy over all non zero values into the zero positions
    for i,num in enumerate(nums):
        if (nums[i] != 0):
            nums[lastModified] = num
            lastModified += 1
    # take the number of modified from above a starting idx, 
    # change the rest of elems until the end into zeroes 
    for i in range(lastModified, len(nums)):
        nums[lastModified] = 0
        lastModified+=1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)