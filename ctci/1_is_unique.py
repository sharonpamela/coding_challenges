# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures? 


import unittest

def is_unique(s):
    
    # if the length of the str is > 256, 
    # which is the valid non-extended ASCII char set, 
    # return false
    if len(s) > 128:
        return False

    seen_map = {}
    for char in s:
        if char in seen_map:
            return False
        else:
            seen_map[char] = 1

    return True

'''
The solution above uses O(n) time as it iterates over the string chars only once.
it has O(n) space as an additional dictionary is needed to keep track of seen values
'''

# if an additional data structure is not allowed, we would have to solve this in place
# this means we would have to compare every char i nthe string to every other char

def is_unique_in_place(s):

    # if no string is provided, return false
    if not s:
        return False

    for i in range (len(s)-1):
        for j in range(i+1,len(s)-1):
            if s[i] == s[j]:
                return False
    return True

'''
The solution above uses no additional data structures BUT has a worse time complexity
as for every char in the string, we have to compare it with every other char in the rest
of the string which yields O(n^2) time for the tradeoff of using O(1) space
'''

class Test(unittest.TestCase):
    def test_is_unique_true(self):
        s = "abcde"
        self.assertTrue(is_unique(s))
    
    def test_is_unique_false(self):
        s = 'abbcde'
        self.assertFalse(is_unique(s))

    def test_is_empty(self):
        s = ''
        self.assertFalse(is_unique(s))

    def test_is_unique_t(self):
        s = "abcde"
        self.assertTrue(is_unique_in_place(s))
    
    def test_is_unique_f(self):
        s = 'abbcde'
        self.assertFalse(is_unique_in_place(s))

unittest.main(verbosity=2)