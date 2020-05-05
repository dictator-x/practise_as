"""
1032. Stream of Characters
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26

class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode()
        self.idx = self.root
        self.s = ""

        for w in words:
            tmp = self.root
            for c in w[::-1]:
                index = ord(c) - ord('a')
                if not tmp.children[index]:
                    tmp.children[index] = TrieNode()
                tmp = tmp.children[index]
            tmp.isWord = True

    def search(self, word):
        tmp = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not tmp.children[index]:
                return False
            tmp = tmp.children[index]
            if tmp.isWord: return True
        return True if tmp.isWord else False

    def query(self, letter: str) -> bool:
        self.s = letter + self.s
        return self.search(self.s)

if __name__ == "__main__":
    words = ["cd","f","kl"]
    checker = StreamChecker(words)
    print(checker.search("cd"))
    print(checker.search("dc"))
    print(checker.search("cda"))
    print(checker.search("f"))

