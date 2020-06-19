"""
322. Coin Change
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        #Initial dp[0] to 0
        dp[0] = 0
        # try each coins.
        for coin in coins:
            for i in range(1, amount+1):
                # May not reachable
                if i - coin >= 0 and dp[i-coin] != -1:
                    if dp[i] == -1:
                        dp[i] = dp[i-coin] + 1
                    else:
                        dp[i] = min([dp[i], dp[i-coin] + 1])
        return dp[-1]
