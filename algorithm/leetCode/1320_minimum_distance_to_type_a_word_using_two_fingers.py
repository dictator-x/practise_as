"""
1320. Minimum Distance to Type a Word Using Two Fingers
"""

import sys

class Solution:
    def minimumDistance(self, word: str) -> int:
        rest = 26
        def cost(a, b):
            if a == rest: return 0
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        # Thinking the idea of mirror equal.
        dp = [ [ -1 ] * 27 for _ in range(len(word)) ]

        def doSearch(idx, o):
            if idx == len(word): return 0
            if dp[idx][o] != -1: return dp[idx][o]

            c = ord(word[idx]) - ord('A')
            p = rest if idx == 0 else ord(word[idx-1]) - ord('A')

            dp[idx][o] = min(doSearch(idx+1, o) + cost(p, c), doSearch(idx+1, p) + cost(o, c))
            return dp[idx][o]

        return doSearch(0, rest)
