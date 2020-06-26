"""
1048. Longest String Chain
"""

from typing import List
from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = [ w for w in sorted(words, key=lambda i: (len(i), i)) ]

        dp = defaultdict(lambda: 0)
        ret = 0
        for w in words:
            for i in range(len(w)):
                pre = w[:i] + w[i+1:]
                dp[w] = max(dp[w], dp[pre]+1)
            ret = max(ret, dp[w])

        return ret

