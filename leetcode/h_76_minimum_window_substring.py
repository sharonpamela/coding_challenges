'''
Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every 
character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 
'A', 'B', and 'C' from string t.
'''

def min_window(s, t):
    if t == "": return ""

    count_t, window = {}, {}
    # initialize count_t with all char counts of t
    for c in t:
        count_t[c] = 1 + count_t.get(c,0)

    have, need = 0, len(count_t)
    res, res_len = [-1, -1], float("inf")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        # does this count satisfy what we need?
        # skip all chars that we don't care about
        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            # update the result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = (r - l + 1)
            # remove chars from the left of the window
            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))