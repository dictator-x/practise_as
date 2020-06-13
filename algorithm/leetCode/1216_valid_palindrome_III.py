"""
1216. Valid Palindrome III
"""

import sys

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        N = len(s)

        dp = [ [100] * N for _ in range(N) ]

        for i in range(N):
            dp[i][i] = 0
            if i < N-1: dp[i][i+1] = 0 if s[i] == s[i+1] else 1

        for l in range(3, N+1):
            for i in range(0, N-l+1):
                j = i+l-1
                if s[i] == s[j]:
                    dp[i][j] = min([dp[i+1][j-1], dp[i+1][j]+1, dp[i][j-1]+1])
                else:
                    dp[i][j] = min([dp[i+1][j-1]+2, dp[i+1][j]+1, dp[i][j-1]+1])

        return True if dp[0][-1] <= k else False
