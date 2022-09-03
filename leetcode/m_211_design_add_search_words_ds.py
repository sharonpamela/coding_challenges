'''
Design a data structure that supports adding new 
words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, 
it can be matched later.
bool search(word) Returns true if there is any string 
in the data structure that matches word or false otherwise. 
word may contain dots '.' where dots can be matched with any letter.
'''
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            if letter in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]    
        node.is_end_of_word = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.is_end_of_word
        return dfs(0, self.root)

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
