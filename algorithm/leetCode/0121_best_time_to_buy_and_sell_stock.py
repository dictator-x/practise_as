"""
121. Best Time to Buy and Sell Stock
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        max_profit = 0
        min_cost = prices[0]

        for price in prices:
            max_profit = max(max_profit, price-min_cost)
            min_cost = min(min_cost, price)

        return max_profit
