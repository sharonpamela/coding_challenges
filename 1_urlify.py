'''
Write a method to replace all spaces in a string with '%20'. 
You may assume that the string
has sufficient space at the end to hold the additional characters, 
and that you are given the "true" length of the string.
'''
import unittest

def urlify(s):
    return '%20'.join(s.split())

'''
time complexity is o(n) bc both .split and .join have to iterate thru n chars.
space complexity is O(n) bc .split creates a list with n items where n is
a char in the input str. 
'''

class Test(unittest.TestCase):
    def test1(self):
        actual = urlify("Mr John Smith   ")
        expected = "Mr%20John%20Smith"
        self.assertEquals(actual, expected)

unittest.main(verbosity=2)