'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

from itertools import zip_longest
from xmlrpc.server import MultiPathXMLRPCServer


def multiply_strings(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    # reverse both numbers
    n1 = num1[::-1]
    n2 = num2[::-1]

    # for each digit in the n2, multiply
    # the digit by n1. store multiplication 
    # result reversed in teh results array
    res = []
    for i, digit in enumerate(n2):
        res.append(multiply_one_digit(digit, i, n1))
    
    # add all results together to get final ans
    ans = add_results(res)
    
    # restore the correct order
    ans.reverse()
    return ''.join(str(n) for n in ans)

def multiply_one_digit (digit2, zero_padding, first_num):
    # pad beginning of current result by based on current digit's 
    # location (1's place -> 0, 10's place -> 1, 100's place -> 2, etc...) 
    curr_res = [0] * zero_padding
    carry = 0

    # multiply all digits in first_num by the current digit of the 
    # second number
    for digit_of_num1 in first_num:
        multiplication = int(digit_of_num1) * int(digit2) + carry
        # carry is set to 10's place digit of multiplication
        carry = multiplication // 10
        # append last digit to the current result
        curr_res.append(multiplication % 10)

    if carry != 0:
        # finished multiplying all digits but there is
        # a carry leftover that needs to be part of solution
        curr_res.append(carry)
    # note: curr_res is still reversed and is an arr of ints
    return curr_res

def add_results(nums):
    cumulative_sum = nums.pop() # start off with one of the nums

    for curr_num in nums:
        new_ans = []
        carry = 0

        # get sum of each digit between curr_num and cumulative_sum
        for digit1, digit2 in zip_longest(curr_num, cumulative_sum, fillvalue=0):
            # add current digit from both numbers
            sum = carry + digit1 + digit2
            carry =  sum // 10 # set to 10's place
            new_ans.append(sum%10) # append 1's place
        if carry != 0:
            new_ans.append(carry)
        
        # update the cumulative_sum in case there are more values to
        # continue to sum
        cumulative_sum = new_ans
    return cumulative_sum

n1= "123"
n2 = "456"
print(multiply_strings(n1, n2))