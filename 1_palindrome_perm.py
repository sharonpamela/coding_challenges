'''
Palindrome Permutation: Given a string, write a function to check 
if it is a permutation of a palindrome. A palindrome is a word or 
phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be 
limited to just dictionary words. 
'''
import unittest

def Palindrome_permutation(s1):
    map1 = {}
    for char in s1:
        if char not in map1:
            map1[char] = 1
        else:
            map1[char] +=1
    
    uneven_count = 0
    for char in map1:
        if map1[char] % 2 != 0:
            uneven_count +=1
        if uneven_count > 1:
            return False
    return True

'''
the solution above is Time O(n) and space O(n).
'''

class Test(unittest.TestCase):
    def test_is_true(self):
        s1 = 'omm'
        expected = True
        actual = Palindrome_permutation(s1)
        self.assertEqual(actual,expected)
    
    def test_is_not_palindrome(self):
        s1 = 'tom'
        expected = False
        actual = Palindrome_permutation(s1)
        self.assertEqual(actual,expected)

unittest.main(verbosity=2)