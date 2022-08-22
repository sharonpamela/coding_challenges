'''
You are given a string s and an integer k. You can choose any character of 
the string and change it to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you 
can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
'''
from collections import Counter

def char_replacement(s, k):
    max_substring_len = 0
    l = 0
    counts = Counter()

    for r in range(len(s)):
        counts[s[r]]+=1

        while (r-l+1) - max(counts.values()) > k:
            counts[s[l]] -= 1
            l += 1
        max_substring_len = max(max_substring_len,  r-l+1)

    return max_substring_len

s = "AABABBA" 
# s = "ABAB"

k = 1
print(char_replacement(s, k))

