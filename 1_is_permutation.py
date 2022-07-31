'''
Check Permutation: Given two strings, write a method to decide 
if one is a permutation of the other.
'''
import unittest

def is_permutation(s1,s2):

    if len(s1) != len(s2):
        return False

    # make a map of chars in s1
    first_str_chars = {}
    for chr in s1:
        if chr in first_str_chars:
            first_str_chars[chr] +=1
        else:
            first_str_chars[chr] = 1
    
    for chr in s2:
        if chr not in first_str_chars:
            return False
        else:
            if first_str_chars[chr] > 1:
                first_str_chars[chr] -= 1
            if first_str_chars[chr] == 1:
                del first_str_chars[chr]
    return len(first_str_chars) == 0


class Test(unittest.TestCase):
    def test_is_true(self):
        s1 = 'abcd'
        s2 = 'dabc'
        self.assertTrue(is_permutation(s1,s2))

    def test_is_false(self):
        s1 = 'abcd'
        s2 = 'afgd'
        self.assertFalse(is_permutation(s1,s2))

unittest.main(verbosity=2)