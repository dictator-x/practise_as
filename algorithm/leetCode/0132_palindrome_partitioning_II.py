"""
132. Palindrome Partitioning II
"""

import sys

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [sys.maxsize]*n
        dp_p = [ [False]*n for _ in range(n) ]

        for i in range(n):
            dp_p[i][i] = True

        for l in range(2, n+1):
            for i in range(0, n-l+1):
                j = i + l -1
                if l == 2:
                    dp_p[i][j] = True if s[i]==s[j] else False
                    continue
                dp_p[i][j] = True if s[i] == s[j] and dp_p[i+1][j-1] else False
        for i in range(n):
            print(dp[i])
            if dp_p[0][i]: dp[i] = 0

            for j in range(0, i):
                if dp_p[j+1][i]:
                    dp[i] = min(dp[i], dp[j]+1)

        return dp[n-1]

