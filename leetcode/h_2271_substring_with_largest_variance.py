'''
The variance of a string is defined as the largest 
difference between the number of occurrences of any 2 
characters present in the string. Note the two characters 
may or may not be the same.

Given a string s consisting of lowercase English letters only, 
return the largest variance possible among all substrings of s.

A substring is a contiguous sequence of characters within a string.
'''
import string

def get_variance(s):
    res = 0
    for c1 in string.ascii_lowercase:
            for c2 in string.ascii_lowercase:
                if c1 != c2:
                    res = max(res, kadane(s,c1, c2))
    return res


# a := the w// higher freq
# b := the w// lower freq
def kadane(s,a,b):
    ans = 0
    countA = 0
    countB = 0
    canExtendPrevB = False
    for c in s:
        print(c)
        if c != a and c != b:
            continue
        if c == a:
            countA += 1
        else:
            countB += 1
        if countB > 0:
            # an interval should contain at least one b
            ans = max(ans, countA - countB)
        elif countB == 0 and canExtendPrevB:
            # edge case: baaaaaa would yield 1 more than it should
            # because b gets set to 0 since its count > a's count 
            # at the beginning
            ans = max(ans, countA - 1)

        # reset if number of b > number of a
        if countB > countA:
            countA = 0
            countB = 0
            canExtendPrevB = True
    return ans

# sample = "aababbb"
# sample = "aabbaaaaca"
sample ="aaaaaaaaabbbb"
# sample ="abbbb"
char1 = 'a'
char2 = 'b'
print(kadane(sample, char1, char2))


# solution below exeeds the time limit for larger inputs because it is n^2
# def get_variance(s):
#     if len(s) == 1:
#         return 0
#     max_variance = 0
#     for i in range(len(s)):
#         for j in range(i,len(s)):
#             curr_sub_array = s[i:j+1]
#             char_counts = Counter(curr_sub_array)
#             curr_variance = max(list(char_counts.values())) - min(list(char_counts.values()))
#             max_variance = max(max_variance, curr_variance)
#     return max_variance
