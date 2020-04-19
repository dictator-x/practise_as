"""
410. Split Array Largest Sum
"""

from typing import List
import sys
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        max_int = sys.maxsize
        # We let m start from 1
        dp = [ [ max_int for _ in range(len(nums)) ] for _ in range(m+1) ]

        # pre sum calculate
        acc_sum =  [ 0 for _ in range(len(nums)) ]
        acc_sum[0] = nums[0]

        for i in range(1, len(nums)):
            acc_sum[i] = acc_sum[i-1] + nums[i]
        # Initial dp, we split entire list input one block
        for i in range(len(nums)):
            dp[1][i] = acc_sum[i]

        #Bottom up calculate
        for i in range(2, m+1):
            # start position j relay on i
            for j in range(i-1, len(nums)):
                # k should have better start position
                # but since I have filled dp with max value.
                # otherwise, it should between[i-2, j)
                for k in range(0, j):
                    dp[i][j] = min(dp[i][j], max(dp[i-1][k], acc_sum[j]-acc_sum[k]) )

        return dp[m][len(nums)-1]
