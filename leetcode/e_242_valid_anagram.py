from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_counts = Counter(s)
        
        for i in t:
            if i in s_counts:
                s_counts[i] -= 1
                if s_counts[i] == 0:
                    del s_counts[i]
        return len(s_counts) == 0