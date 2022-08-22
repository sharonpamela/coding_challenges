'''
Given an integer array nums, return all the 
triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and 
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain 
duplicate triplets.
'''

from collections import Counter

def find_3sum(nums):
    res = []
    nums.sort()
    for i,num in enumerate(nums):
        if num > 0:
            break
        if i == 0 or num != nums[i-1] :
            find_2sum(nums, i, res)
    return res

def find_2sum(nums, i, res):
    l = i+1
    r = len(nums)-1
    while l < r:
        curr_sum = nums[l] + nums[r] + nums[i]
        if  curr_sum < 0:
            l += 1
        elif curr_sum > 0:
            r -= 1
        else:
            # curr_sum == 0
            l += 1
            r -= 1
            res.append(([nums[l],nums[r],nums[i]]))
            # advance l if next value is the same
            while l < r and nums[l] != nums[i-1]:
                l += 1
        


# first attempt:
    # if len(nums) < 3:
    #     return []

    # counts = Counter(nums)
    # print(f"counts {counts}")
    # triplets = set()
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         n1 = nums[i]
    #         n2 = nums[j]
    #         last_num = n1 + n2
    #         last_num_opposite = -last_num
    #         if last_num_opposite in counts:
    #             # remove it from the counts so 
    #             # it can't be used for another combo
    #             # so i != j, i != k, and j != k
    #             print(f"Found n1 {n1} n2 {n2} and complement {last_num_opposite}")
    #             remove_from_count(counts, last_num_opposite)
    #             remove_from_count(counts, n1)
    #             remove_from_count(counts, n2)
    #             t_list = [n1,n2,last_num_opposite]
    #             t_list.sort()
    #             triplets.add(tuple(t_list))
    #     return triplets

    # def remove_from_count(counts, num):
    #     counts[num] -= 1
    #     if counts[num] == 0:
    #         counts.pop(num)

# No sort:
# def find_3sum(nums):
#     res, dups = set(), set()
#     seen = {}
#     for i, val1 in enumerate(nums):
#         if val1 not in dups:
#             dups.add(val1)
#             for val2 in nums[i+1:]:
#                 complement = -val1 - val2
#                 if complement in seen and seen[complement] == i:
#                     res.add(tuple(sorted((val1, val2, complement))))
#                 seen[val2] = i
#     return res

nums = [-1,0,1,2,-1,-4]
# nums = [1,2,-2,-1]
print(find_3sum(nums))
