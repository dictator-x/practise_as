"""
387. First Unique Character in a String
"""

from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        record = defaultdict(lambda: 0)

        for c in s:
            record[c] += 1

        for idx, c in enumerate(s):
            if record[c] == 1:
                return idx
        return -1
