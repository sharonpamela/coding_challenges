'''
Given an integer array nums, return an array answer 
such that answer[i] is equal to the product of all the 
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and 
without using the division operation.
'''

def product_except_self(nums):

    l_to_r = [1] * len(nums) # A
    r_to_l = [1] * len(nums) # B 

    #     [ 2,        4,       5,      1       ] original
    #     [ 4*5*1,    2*5*1,   2*4*1,  2*4*5   ] needed response

    #    A[ - ,       2        2*4,    2*4*5   ] left to right w/o curr idx
    #    B[ 4*5*1     5*1      1        -      ] right to left w/o curr idx
    #     [ 4*5*1,    2*5*1,   2*4*1,  2*4*5   ] multiplying A and B idx per idx
    
    for i in range(1, len(nums)):
        l_to_r[i] = l_to_r[i-1] * nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        r_to_l[i] = r_to_l[i+1] * nums[i+1]
    
    for i in range(len(nums)):
        l_to_r[i] *= r_to_l[i]

    return l_to_r

nums = [-1,1,0,-3,3]  
nums = [1,2,3,4] 
print(product_except_self(nums))