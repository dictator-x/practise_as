"""
123. Best Time to Buy and Sell Stock III
"""

import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost1, cost2 = sys.maxsize, sys.maxsize
        profit1, profit2 = 0, 0

        for price in prices:
            cost1 = min(cost1, price)
            profit1 = max(profit1, price - cost1)

            cost2 = min(cost2, price - profit1)
            profit2 = max(profit2, price - cost2)

        return profit2
