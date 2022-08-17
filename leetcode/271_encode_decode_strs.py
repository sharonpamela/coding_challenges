'''
Design an algorithm to encode a list of 
strings to a string. The encoded string 
is then sent over the network and is 
decoded back to the original list of 
strings.
'''

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.
        """
        res = ""

        for s in strs:
            res += str(len(s)) + '#' + s
         
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            # j is now at delimiter '#'
            str_len = int(s[i:j])
            res.append( s[j + 1 : j + 1 + str_len])
            i = j + 1 + str_len
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))