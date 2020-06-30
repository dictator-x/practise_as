"""
819. Most Common Word
"""

from typing import List
from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        M = defaultdict(lambda: 0)

        for word in paragraph.lower().split():
            M[word] += 1

        count = 0
        ret = ""
        print(M)
        for word, c in M.items():
            if c > count and word not in banned:
                ret = word
                count = c
        return ret
