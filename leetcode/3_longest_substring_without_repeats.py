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



# less cleaner approach than the one above
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        
        low_idx = 0
        counter = collections.Counter()
        max_seen = set()
        idx = 0
        while idx < len(s):
            counter[s[idx]]+=1
            max_seen.add(len(counter))
            if counter[s[idx]] == 2:
                # case 1: value at idx matches value at low_idx
                # just increate low_idx
                if s[low_idx] == s[idx]:
                    counter[s[low_idx]] -= 1
                    low_idx+=1

                # case 2:calue at idz doesn't match value at low_idx
                # advance low_idx until the value matches value at idx
                # delete the letters that have been found along the way
                else:
                    while s[low_idx] != s[idx] and low_idx != idx:
                        counter[s[low_idx]] -= 1
                        if counter[s[low_idx]] == 0:
                            counter.pop(s[low_idx])
                        low_idx+=1
                    counter[s[low_idx]] -= 1
                    if counter[s[low_idx]] == 0:
                        counter.pop(s[low_idx])
                    low_idx+=1 # advance start to not include repeated elem

            idx+=1   
        return (max(max_seen))

'''