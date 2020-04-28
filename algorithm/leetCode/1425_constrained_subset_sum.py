"""
1425. Constrained Subset Sum
"""

from typing import List
import sys

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        nums_len = len(nums)
        dp = [0] * nums_len
        # m queue
        queue = []
        ret = - sys.maxsize
        for i in range(nums_len):
            # Remove from queue
            if k < i and i-k-1 == queue[0]:
                queue.pop(0)

            dp[i] = max(dp[queue[0]] if len(queue) != 0 else 0, 0) + nums[i]

            while len(queue) > 0 and dp[i] >= dp[queue[-1]]:
                queue.pop()

            queue.append(i)
            ret = max(ret, dp[i])
        return ret
