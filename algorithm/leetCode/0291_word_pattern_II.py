"""
291. Word Pattern II
"""

class Solution:
    def wordPatternMatch(self, pattern: str, string: str) -> bool:
        m = {}
        s = set([])
        def isMatch(pattern, string):
            n_p = len(pattern)
            n_s = len(string)
            if n_p == 0 and n_s == 0:
                return True
            if n_p == 0 or n_s == 0:
                return False

            c_p = pattern[0]

            if c_p in m:
                if not string.startswith(m[c_p]): return False
                else: return isMatch(pattern[1:], string[len(m[c_p]):])

            for i in range(1, n_s+1):
                if string[0:i] in s: continue

                m[c_p] = string[0:i]
                s.add(m[c_p])
                if isMatch(pattern[1:], string[i:]): return True
                s.remove(m[c_p])
                del m[c_p]

            return False

        return isMatch(pattern, string)

