'''
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
'''
def next_perm(nums):
    # search for decreasing elem from right to left and 
    i = len(nums) - 2
    while i >= 0 and nums[i+1] <= nums[i]:
        # start from second to last elem so i stops on the target elem 
        # that needs swapping
        i -= 1
    print(f"nums {nums} found i {i} at elem {nums[i]}")
    if i >= 0:
        # find the number just below or eq to the target elem
        # start from the back of array
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        print(f"nums {nums} found j {j} at elem {nums[j]}. swapping with elem {nums[i]}")
        # swap the elems
        nums[j], nums[i] = nums[i], nums[j]

    # reverse all other elems from target elem to end of array
    start = i+1
    end = len(nums)-1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        end -=1
        start +=1
    return nums




# print(f"Next perm of [9,5,4,3,1] expected: [1,3,4,5,9] actual: {next_perm([9,5,4,3,1])}")
# print(f"Next perm of [9,4,3,5,1] expected: [9,4,5,1,3] actual: {next_perm([9,4,3,5,1])}")
# print(f"Next perm of [1,2,3] expected:[1,3,2]  actual: {next_perm([1,2,3])}")
# print(f"Next perm of [3,2,1] expected: [1,2,3]  actual: {next_perm([3,2,1])}")
arr = [1,3,2]
# arr = [1,2,3]
# print(f"Next perm of [1,3,2] expected: [2,1,3] {next_perm(arr)}")
next_perm(arr)
print(arr)


# def next_perm(arr):
#     if len(arr) == 2:
#         arr[0], arr[1] = arr[1], arr[0]
#         return arr

#     i = len(arr)-1
#     target_left = None
#     target_left_idx = None
    
#     while i > 0:
#         # find number x from right to left that decreases
#         if arr[i-1] < arr[i]:
#             target_left = arr[i-1]
#             target_left_idx = i-1
#             break
#         i-=1
#     # if exited this loop and target_left is still none,
#     # then there is no posible next perm larger, need to return the smallest
#     if target_left is None:
#        arr.sort()
#        return arr
 
#     # starting at index of x+1 left to right, find number y
#     # that is just bigger than number x
#     j = target_left_idx+1
#     while j <= len(arr)-1:
#         if target_left > arr[j]:
#             just_bigger_idx = j-1
#             # swap x and y
#             arr[just_bigger_idx], arr[target_left_idx] = arr[target_left_idx], arr[just_bigger_idx]
#             break
#         j+=1
#     print(arr)
#     # reverse all nums from original x's index+1 to the end 
#     arr_end = len(arr)-1
#     first_idx_to_reverse = target_left_idx+1
#     while first_idx_to_reverse < arr_end:
#         print("reversing")
#         arr[first_idx_to_reverse], arr[arr_end] = arr[arr_end], arr[first_idx_to_reverse]
#         print(arr)
#         arr_end -=1
#         first_idx_to_reverse +=1
#     return arr