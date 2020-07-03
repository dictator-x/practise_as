"""
70. Climbing Stairs
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[n] = dp[n-1] + dp[n-2]

        return dp[-1]

