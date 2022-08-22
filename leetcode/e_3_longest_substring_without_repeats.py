
'''
Given a string s, find the length of the 
longest substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''

import collections

def find_longest_substring(s):

    low_idx = 0
    counter = collections.Counter()
    max_seen = 0
    idx = 0
    while idx < len(s):
        # increase count of current elem
        counter[s[idx]]+=1
       
        '''check for repeated elems in counter
        case 1: value at idx matches value at low_idx
        matches case when s[low_idx] == s[idx]
        so advance low_idx until 1 spot after curr location
        
        case 2: value at idx doesn't match value at low_idx
        so advance low_idx until 1 spot after first value 
        encountered that matches current value at idx'''  
        while counter[s[idx]] > 1:

            # delete the letters that had been found along the way
            # while making correction
            counter[s[low_idx]] -= 1
            low_idx+=1

        # log the max length seen thus far
        max_seen = max(max_seen, idx-low_idx+1)

        idx+=1   
    return max_seen

print(find_longest_substring("abcabcbb"))


# another aproach:
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