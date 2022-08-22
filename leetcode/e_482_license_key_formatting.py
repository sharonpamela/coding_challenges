# We want to reformat the string s such that each group 
# contains exactly k characters, except for the first group, 
# which could be shorter than k but still must contain at 
# least one character. Furthermore, there must be a dash 
# inserted between two groups, and you should convert all 
# lowercase letters to uppercase.

# Return the reformatted license key.

def reformat_license(s,k):
    res = []
    curr_k = k
    for i in range(len(s)-1, -1, -1):
        if curr_k > 0 and s[i] != '-':
            res.append(s[i].upper())
            curr_k -= 1
        elif curr_k == 0:
            res.append("-")
            if s[i] != '-':
                res.append(s[i].upper())
                curr_k = k-1
            else:
                curr_k = k
    if res and res[-1] == "-":
        res.pop()
    reverse_l(res)
    return("".join(res))

def reverse_l (s):
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

s = "5F3Z-2e-9-w"
# s = "2-4A0r7-4k"
# s = "--a-a-a-a--"
# s = "---"
k = 4
print(reformat_license(s,k))