"""
188. Best Time to Buy and Sell Stock IV
"""

from typing import List

class Solution:
    # Too expensive
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        # Optimize1: k >= n//2 means => Best Time to Buy and Sell Stock II.
        n = len(prices)
        if k >= n//2:
            ret = 0
            for i in range(1, len(prices)):
                ret += max(0, prices[i] - prices[i-1])
            return ret

        n = len(prices)
        dp = [ [0] * (n) for _ in range(k+1) ]

        for i in range(1, k+1):
            cost = prices[0]
            for j in range(1, n):
                # has highest value before dp[i][j]
                dp[i][j] = dp[i][j-1]

                # for m in range(0, j):
                #     dp[i][j] = max(dp[i][j], prices[j]-prices[m]+dp[i-1][m])

                dp[i][j] = max(dp[i][j], prices[j] - cost)
                cost = min(cost, prices[j] - dp[i-1][j-1])
        return dp[-1][-1]

