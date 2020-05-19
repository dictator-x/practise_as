"""
115. Distinct Subsequences
"""

# worth to review
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(t), len(s)
        dp = [ [0] * (m+1) for _ in range(n+1) ]

        # understand why initial value is 1.
        for i in (m):
            dp[0][i] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]
