''''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to 
target.

You may assume that each input would have exactly one 
solution, and you may not use the same element twice.

You can return the answer in any order.
'''


def two_sum(nums, target):

    possible_complements = {}

    for i,n in enumerate(nums):
        # n1 + n2 = target => n1 = target - n2
        diff = (target - n)
        if diff in possible_complements:
            return [possible_complements[diff], i]
        possible_complements[n] = i
    return []


print(two_sum([2,7,11,15],9))
