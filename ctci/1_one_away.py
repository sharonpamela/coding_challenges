'''
One Away: There are three types of edits that can be performed on 
strings: insert a character, remove a character, or replace a character. 
Given two strings, write a function to check if they are
one edit (or zero edits) away
'''

import unittest

def One_way(s1,s2):
    if len(s1) == len(s2):
        return one_edit(s1, s2)
    else:
        if len(s1)+1 == len(s2):
            return one_edit(s1,s2)
        elif len(s1)-1 == len(s2):
            return one_edit(s2,s1)
    return False

def one_edit(w1,w2):
    '''
    returns true if only one edit is needed (insert or replace).
    false otherwise
    '''
    one_edit_used = False
    is_equal_len = len(w1) == len(w2)
    w1_idx = 0
    w2_idx = 0
    while (w1_idx < len(w1) and w2_idx < len(w2)):
        if w1[w1_idx] != w2[w2_idx]:
            if one_edit_used:
                return False
            if not is_equal_len:
                w2_idx +=1
            one_edit_used = True
        w1_idx +=1
        w2_idx +=1
    return True


# def one_replace(w1, w2):
#     Returns True if only one replacement is needed to 
#     be made on w1 to make it the same as w2
#     '''
#     one_replaced_used = False
#     w1_idx = 0
#     w2_idx = 0
#     for _ in range(len(w2)-1):
#         if w1[w1_idx] != w2[w2_idx]:
#             if one_replaced_used:
#                 return False
#             one_replaced_used = True
#         w1_idx +=1
#         w2_idx +=1
#     return True

# def one_insert(short_word, long_word):
#     '''
#     returns true if only one insertion is needed into w1 for
#     it to equal w2. False otherwise
#     '''
#     one_insert_used = False
#     short_idx = 0
#     long_idx = 0
#     for _ in range(len(long_word)-1):
#         if short_word[short_idx] != long_word[long_idx]:
#             if one_insert_used:
#                 return False
#             # advance the long word idx to pretend we inserted
#             # into the short word
#             long_idx +=1
#             one_insert_used = True
#         short_idx+=1
#         long_idx+=1
#     return True
    
class Test(unittest.TestCase):
    def test_1(self):
        s1= 'apple'
        s2= 'aple'
        expected = True
        actual = One_way(s1,s2)
        self.assertEqual(actual, expected)

    def test_2(self):
        s1= 'pale'
        s2= 'ple'
        expected = True
        actual = One_way(s1,s2)
        self.assertEqual(actual, expected)

    def test_3(self):
        s1= 'applee'
        s2= 'aple'
        expected = False
        actual = One_way(s1,s2)
        self.assertEqual(actual, expected)

    def test_4(self):
        s1= 'taco'
        s2= 'tatos'
        expected = False
        actual = One_way(s1,s2)
        self.assertEqual(actual, expected)

    def test_5(self):
        s1= 'pales'
        s2= 'pale'
        expected = True
        actual = One_way(s1,s2)
        self.assertEqual(actual, expected)

    def test_6(self):
        s1= 'pale'
        s2= 'bale'
        expected = True
        actual = One_way(s1,s2)
        self.assertEqual(actual, expected)   

    def test_7(self):
        s1= 'pale'
        s2= 'bake'
        expected = False
        actual = One_way(s1,s2)
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)