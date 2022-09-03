'''
Given an array of distinct integers candidates and a target 
integer target, return a list of all unique combinations of 
candidates where the chosen numbers sum to target. You may 
return the combinations in any order.

The same number may be chosen from candidates an unlimited 
number of times. Two combinations are unique if the frequency 
of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that 
sum up to target is less than 150 combinations for the given input.
'''

from re import I


def combinationSum(candidates, target):
    '''
    [2,3,5] target = 8

    2 2 2 2 = 8                 
    2 3 3 = 8
    3 5 = 8

    8 - 2 = 6                   8 - 5 = 3

    6 - 2 = 4                   3 - 2 = 1 (not feasible)
    6 - 3 = 3                   3 - 3 = 0 
    6 - 5 = 1 (not feasible)

    4 - 2 = 2
    4 - 3 = 1 (not feasible)

    3 - 3 = 0
    2 - 2 = 0
    '''
    res = []
    def dfs(i, cur, total):
        if total == target:
            res.append([x for x in cur])
            return
        if i >= len(candidates) or \
        total > target:
            return
        
        cur.append(candidates[i])
        dfs(i, cur, total+candidates[i])
        cur.pop()
        dfs(i+1, cur, total)
    
    dfs(0,[],0)
    return res
