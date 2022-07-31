'''
String Rotation:Assume you have a method isSubstring which 
checks if oneword is a substring
of another. Given two strings, sl and s2, write code to 
check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat"). 
'''
import unittest

def isSubstring(s1,s2):

    if not s1 or not s2:
        return False
        
    rotations = s1+s1
    substr_first_char = s2[0]
    # search for the potential starting pt 
    # of the rotation (if valid substr, this will 
    # be within the len of the s1 str)
    for i in range(len(s1)):
        if rotations[i] == substr_first_char:
            # found possible rotation start
            possible_substr = rotations[i:i+len(s2)]
            if possible_substr == s2:
                return True
    return False

class Test(unittest.TestCase):
    def test_1(self):
        s1 = 'dish'
        s2 = 'ishd'
        self.assertTrue(isSubstring(s1, s2))
        
    def test_2(self):
        s1 = 'disk'
        s2 = 'ishd'
        self.assertFalse(isSubstring(s1, s2))


unittest.main(verbosity=2)