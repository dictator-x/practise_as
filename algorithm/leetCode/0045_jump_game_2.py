"""
45. Jump Game II
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        ret = 0
        maxSeen = 0
        curMax = 0
        for i in range(len(nums) - 1):
            maxSeen = max(maxSeen, nums[i]+i)
            print(ret)
            if curMax == i:
                ret += 1
                curMax = maxSeen
        return ret
