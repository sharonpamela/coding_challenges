from collections import Counter

def countCharacters(self, words: List[str], chars: str) -> int:
    char_map = Counter(chars)
    totals = 0
    for word in words:
        char_map = Counter(chars)
        for i,c in enumerate(word):
            if char_map.get(c) and char_map.get(c) > 0:
                char_map[c] -= 1
                if char_map.get(c) == 0:
                    del char_map[c]
                if i == len(word) -1: totals += len(word)
            else:
                break
        
    return totals

    # another aproach
    
# def countCharacters(self, words: List[str], chars: str) -> int:
#         res=0
#         for i in words:
#             for j in i:
#                 if(i.count(j)>chars.count(j)):
#                     break
#             else:
#                 res+=len(i)
#         return res
