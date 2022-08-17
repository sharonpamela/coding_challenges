'''
Given a string s, find the length of the 
longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

def longest_substr(s):
    l = 0
    seen =  set()
    max_seen = 0
    for r in range(len(s)):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        max_seen = max(max_seen, r-l+1)
    return max_seen

s = "abcabcbb"
s = "bbbbb"
s= "pwwkew"
print(longest_substr(s))