"""
33. Search in Rotated Sorted Array
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target: return m

            # total four possibles in each branch.
            # 8 possibilities in total.
            if target >= nums[0]:
                if nums[m] >= nums[0] and nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] < nums[0] and nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

        return -1
