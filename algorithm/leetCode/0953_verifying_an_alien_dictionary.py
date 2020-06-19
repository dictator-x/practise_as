"""
953. Verifying an Alien Dictionary
"""

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_ascii = {}
        for i, c in enumerate(order):
            alien_ascii[c]=i

        def word1_GTE_word2(word1, word2):
            N = len(word1) if len(word1) <= len(word2) else len(word2)
            for i in range(N):
                if word1[i] == word2[i]:
                    continue
                return True if alien_ascii[word1[i]] < alien_ascii[word2[i]] else False

            return True if len(word1) <= len(word2) else False

        for word1, word2 in zip(words, words[1:]):
            if not word1_GTE_word2(word1, word2):
                return False
        return True
