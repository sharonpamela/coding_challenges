'''
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all 
the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''

from collections import defaultdict


def group_anagrams(strs):

    ans = {} # key is sorted anagram and value is list of strs

    # determine if the current anagram is unique
    # if so, add it to a new list
    # else, add this anagram to the list it belongs
    for s in strs:
        sorted_string = "".join(sorted([char for char in s]))
        if sorted_string not in ans:
            ans[sorted_string] = [s]
        else:
            ans[sorted_string].append(s)
        
    return ans.values()
'''
the solution above has time complexity (m * n log n) 
where n is the average length of every input str and m is 
how many input strings we must sort
'''


# another aproach that doesn't use sorting is below
def group_anagrams2(strs):
    # takes advantage of the fact we can create a unique key
    # based on the letters seen in a str, which will be the
    # same between anagrams and will yield the correct group mapping

    ans = defaultdict(list)

    for s in strs:
        counts = [0] * 26

        # create current str's anagram id
        for char in s:
            a_idx = ord(char) - ord('a')
            counts[a_idx] += 1

        ans[tuple(counts)].append(s)
    return ans.values()

        


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))