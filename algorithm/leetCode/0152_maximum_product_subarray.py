"""
152. Maximum Product Subarray
"""

from typing import List
import sys

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_max, pre_min = nums[0], nums[0]
        ret = nums[0]
        for val in nums[1:]:
            cur_max = max([pre_max*val, pre_min*val, val])
            cur_min = min([pre_max*val, pre_min*val, val])

            pre_max = cur_max
            pre_min = cur_min

            ret = max(ret, cur_max)

        return ret
