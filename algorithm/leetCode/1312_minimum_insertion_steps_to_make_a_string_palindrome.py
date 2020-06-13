"""
1312. Minimum Insertion Steps to Make a String Palindrome
"""
import sys

class Solution:
    def minInsertions(self, s: str) -> int:
        N = len(s)
        dp = [ [100] * N for _ in range(N) ]

        # Initial s[i:i] to 0
        for i in range(N):
            dp[i][i] = 0

        # Initial s[i:i+1]
        for i in range(N-1):
            if s[i] == s[i+1]: dp[i][i+1] = 0
            else: dp[i][i+1] = 1

        for l in range(3, N+1):
            for i in range(0, N-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = min([dp[i+1][j-1], dp[i+1][j]+1, dp[i][j-1]+1])
                else:
                    dp[i][j] = min([dp[i+1][j-1]+2, dp[i+1][j]+1, dp[i][j-1]+1])

        return dp[0][-1]
