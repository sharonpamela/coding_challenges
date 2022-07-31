'''
String Compression: Implement a method to 
perform basic string compression using the counts
of repeated characters. For example, the string 
aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than 
the original string, your method should return
the original string. You can assume the string
has only uppercase and lowercase letters (a - z). 
'''
import unittest

def compress_string(s):

    curr_char_count = 0
    res = []

    for i in range(len(s)):
        
        curr_char_count +=1
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
        if i+1 >= len(s) or s[i+1] != s[i]:
            res.append(s[i] + str(curr_char_count))
            curr_char_count = 0

    compressed_str = "".join(res)
 
    # only return the compressed str if it is less than 
    # the orig str
    return compressed_str if len(compressed_str) < len(s) else s

class Test(unittest.TestCase):
    def test_1(self):
        s = 'aabcccccaan'
        expected = 'a2b1c5a2n1'
        actual = compress_string(s)
        self.assertEqual(expected,actual)

    def test_2(self):
        s = 'aabcccccaa'
        expected = 'a2b1c5a2'
        actual = compress_string(s)
        self.assertEqual(expected,actual)

    def test_3(self):
        s = 'abc'
        expected = 'abc'
        actual = compress_string(s)
        self.assertEqual(expected,actual)

    def test_4(self):
        s = 'eettttttttttttyyyyyyyyyy'
        expected = 'e2t12y10'
        actual = compress_string(s)
        self.assertEqual(expected,actual)
unittest.main(verbosity=2)


# old version (this version was simplified to the version above)

# def compress_string(s):

#     curr_char = s[0]
#     curr_char_count = 1

#     res = []

#     for i in range(1,len(s)):
#         if s[i] == curr_char:
#             curr_char_count +=1
        
#         if i == len(s)-1:
#             # we we are on the last char and this is a different char
#             if not curr_char_count:
#                 curr_char_count+=1
#             res.append(curr_char + str(curr_char_count))
#         else:
#             if s[i+1] != curr_char:
#                 res.append(curr_char + str(curr_char_count))
#                 curr_char_count = 0
#                 curr_char = s[i+1]
#     compressed_str = "".join(res)
 
#     # only return the compressed str if it is less than 
#     # the orig str
#     return compressed_str if len(compressed_str) < len(s) else s