"""
363. Max Sum of Rectangle No Larger Than K
"""

from typing import List
from bisect import bisect_left, insort_left
import sys

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], K: int) -> int:
        n_row, n_col = len(matrix), len(matrix[0])
        ret = - sys.maxsize
        for i in range(n_row):
            # Record sum in vertical
            dp = [0] * n_col
            for j in range(i, n_row):
                pre_sum = [0]
                cur_val = 0
                for k in range(n_col):
                    dp[k] += matrix[j][k]
                    cur_val += dp[k]

                    # why cur_val - k
                    idx = bisect.bisect_left(pre_sum, cur_val - K)

                    if idx != len(pre_sum):
                        ret = max(ret, cur_val - pre_sum[idx])
                    insort_left(pre_sum, cur_val)
        return ret


