"""
1397. Find All Good Strings
"""

from functools import lru_cache
# KMP + dp
# using KMP to quick compare with evil
class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        # evil in the pattern
        def prepareKMPArray(pattern):
            n = len(pattern)
            ret = [0] * (n+1)
            # Initial position 0 to -1
            ret[0] = -1

            i = 0
            j = -1

            while i < n:
                while j != -1 and pattern[i] != pattern[j]:
                    j = ret[j]
                i += 1
                j += 1
                ret[i] = j

            return ret

        mod = 10**9 + 7
        n_s = n
        n_evil = len(evil)
        kmp_next = prepareKMPArray(evil)

        @lru_cache(maxsize=None)
        def dfs_s1(idx_s, idx_evil, up_margin):
            # Bad string end.
            if idx_evil == n_evil: return 0
            # Good string end.
            if idx_s == n_s: return 1

            possible = s1[idx_s] if up_margin else "z"
            ret = 0
            # Key of whole calculation.
            for i in range(ord("a"), ord(possible)+1):
                # set up filter for Bad string.
                # should be local for each iteration
                cur = idx_evil
                while cur != -1 and evil[cur] != chr(i):
                    cur = kmp_next[cur]
                ret += dfs_s1(idx_s+1, cur+1, up_margin and (i==ord(possible)))
            return ret % mod

        @lru_cache(maxsize=None)
        def dfs_s2(idx_s, idx_evil, up_margin):
            # Bad string end.
            if idx_evil == n_evil: return 0
            # Good string end.
            if idx_s == n_s: return 1

            possible = s2[idx_s] if up_margin else "z"
            ret = 0
            for i in range(ord("a"), ord(possible)+1):
                # set up filter for Bad string.
                # should be local for each iteration
                cur = idx_evil
                while cur != -1 and evil[cur] != chr(i):
                    cur = kmp_next[cur]
                ret += dfs_s2(idx_s+1, cur+1, up_margin and (i==ord(possible)))
            return ret % mod

        ret = ( dfs_s2(0, 0, True) - dfs_s1(0, 0, True) + mod ) % mod
        if s1.find(evil) == -1: ret += 1
        return ret
