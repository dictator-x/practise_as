"""
438. Find All Anagrams in a String
"""

from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        chars = [0]*26
        window = [0]*26

        for c in p:
            chars[ord(c)-ord("a")] += 1

        n_p = len(p)

        ret = []
        for idx, c in enumerate(s):
            if idx >= n_p:
                window[ord(s[idx-n_p])-ord("a")] -= 1

            window[ord(c)-ord("a")] += 1
            if chars == window:
                ret.append(idx-n_p+1)

        return ret
