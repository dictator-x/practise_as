"""
1235. Maximum Profit in Job Scheduling
"""

from typing import List

# key is to sort with endTime.
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        items = []

        for start, end, pro in zip(startTime, endTime, profit):
            items.append((start, end, pro))

        items.sort(key=lambda i: i[1])

        dp = [0] * len(items)


        # Initial profit for job[i]
        for i in range(len(items)):
            dp[i] = items[i][2]

        for i in range(1, len(items)):
            # Carryover max profit
            dp[i] = max(dp[i-1], dp[i])
            #TODO: use binary search to improve
            for j in range(i-1,-1,-1):
                if items[i][0] >= items[j][1]:
                    dp[i] = max(dp[i], items[i][2] + dp[j])
                    break
        return dp[len(items)-1]
