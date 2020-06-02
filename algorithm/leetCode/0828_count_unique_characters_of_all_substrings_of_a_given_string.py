"""
828. Count Unique Characters of All Substrings of a Given String
"""

from collections import defaultdict

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        mod = 10 ** 9 + 7
        char_index = defaultdict(list)

        for i, v in enumerate(s):
            char_index[v].append(i)

        ret = 0

        for v in char_index.values():
            v = [-1] + v + [len(s)]
            for i in range(1, len(v)-1):
                ret += (v[i] - v[i-1]) * (v[i+1] - v[i])
        return ret % mod
