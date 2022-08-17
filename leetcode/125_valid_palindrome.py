'''
A phrase is a palindrome if, after converting all uppercase 
letters into lowercase letters and removing all non-alphanumeric 
characters, it reads the same forward and backward. Alphanumeric 
characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false 
otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''

def is_valid_palindrome(s):
    new_s = ''.join(char for char in s if char.isalnum())
    new_s = new_s.lower()
    l = 0
    r = len(new_s)-1
    while l < r:
        if new_s[l] != new_s[r]:
            return False
        l+=1
        r-=1
    return True

s = "A man, a plan, a canal: Panama"
print(is_valid_palindrome(s))