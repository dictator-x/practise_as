"""
16. 3Sum Closest
"""

from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        ret = sum([nums[0], nums[1], nums[2]])

        for i in range(0, N-2):
            lo, hi = i+1, N-1
            cur = nums[i]

            while lo < hi:
                tmp = nums[lo]+nums[hi]+cur
                if tmp == target: return target
                elif tmp < target:
                    lo += 1
                else:
                    hi -= 1
                if abs(tmp-target) < abs(ret-target):
                    ret = tmp

        return ret
