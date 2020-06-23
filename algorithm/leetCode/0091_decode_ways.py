"""
91. Decode Ways
"""

from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        def isValid(s):
            if 1 <= int(s) <= 26:
                if s[0] == "0": return False
                return True
            else:
                return False

        @lru_cache(maxsize=None)
        def search(s):
            if s == "": return 1

            ret = 0
            for i in range(1, 3):
                if len(s) >= i:
                    head = s[0:i]
                    tail = s[i:]
                    if isValid(head):
                        ret += search(tail)

            return ret
        return search(s)
