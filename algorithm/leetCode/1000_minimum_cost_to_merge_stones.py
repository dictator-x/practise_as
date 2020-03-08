"""
1000. Minimum Cost to Merge Stones
"""

from typing import List
import sys

class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        INT_MAX = sys.maxsize
        n = len(stones)
        if (n-1) % (K-1) != 0:
            return -1
        presum = [0] * (n+1)

        for i in range(n):
            presum[i+1] = presum[i] + stones[i]

        dp = [ [ INT_MAX for _ in range(n) ] for _ in range(n) ]

        for i in range(n):
            dp[i][i] = 0

        for l in range(2, n + 1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                for m in range(i, j, K-1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j])
                if (l - 1) % (K-1) == 0:
                    dp[i][j] = dp[i][j] + presum[j+1] - presum[i]
        return dp[0][n-1]
