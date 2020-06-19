"""
560. Subarray Sum Equals K
"""
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_count = defaultdict(lambda: 0)
        pre_count[0] = 1

        pre_sum = 0
        ret = 0
        for n in nums:
            pre_sum += n
            ret += pre_count[pre_sum-k]
            pre_count[pre_sum] += 1
        return ret
