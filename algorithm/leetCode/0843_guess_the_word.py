"""
843. Guess the Word
"""

class Master:
    def guess(self, word: str) -> int:

from random import randint

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        def match(a, b):
            ret = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    ret += 1
            return ret

        def updateWordlist(wordlist, guess, matches):
            ret = []
            for word in wordlist:
                if ( match(word, guess) == matches ):
                    ret.append(word)
            return ret

        temp = wordlist
        for _ in range(10):
            guess = temp[randint(0, len(temp)-1)]
            m = master.guess(guess)
            temp = updateWordlist(temp, guess, m)


