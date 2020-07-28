"""
523. Continuous Subarray Sum
"""

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        record = {}
        acc = 0
        record[0] = -1

        for idx, n in enumerate(nums):
            acc += n

            if k != 0:
                acc = acc % k

            if acc in record:
                if idx - record[acc] > 1:
                    return True
            else:
                record[acc] = idx
        return False
