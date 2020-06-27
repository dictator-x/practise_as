"""
209. Minimum Size Subarray Sum
"""

from typing import List
import sys

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        sums = 0
        ret = sys.maxsize
        j = 0
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s and j <= i:
                ret = min(ret, i-j+1)
                sums -= nums[j]
                j += 1
        return ret if ret != sys.maxsize else 0
