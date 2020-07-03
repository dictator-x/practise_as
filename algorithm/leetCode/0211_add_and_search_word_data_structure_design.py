"""
211. Add and Search Word - Data structure design
"""

class TrieNode:
    def __init__(self, isWorld=False):
        self.children = [None] * 26
        self.isWorld = isWorld
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tmp = self.root
        for c in word:
            if not tmp.children[ord(c)-ord("a")]:
                tmp.children[ord(c)-ord("a")] = TrieNode()
            tmp = tmp.children[ord(c)-ord("a")]
        tmp.isWorld = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def doSearch(root, word, idx):
            if idx == len(word):
                return root.isWorld

            c = word[idx]
            if c == ".":
                for i in range(26):
                    if root.children[i] and doSearch(root.children[i], word, idx+1): return True
                return False
            else:
                return root.children[ord(c)-ord("a")] and doSearch(root.children[ord(c)-ord("a")], word, idx+1)

        return doSearch(self.root, word, 0)
