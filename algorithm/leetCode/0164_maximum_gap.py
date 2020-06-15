"""
164. Maximum Gap
"""

from typing import List
from math import ceil

#from math import ceil
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        min_value = min(nums)
        max_value = max(nums)
        N = len(nums)

        avg_gap = max(1, (max_value - min_value) // (N-1))
        bucket_size = ceil((max_value - min_value + 1)/avg_gap)
        bucket = [ [] for _ in range(bucket_size) ]
        for value in nums:
            bucket_index = (value - min_value) // avg_gap
            bucket[bucket_index].append(value)

        nums = []
        for slot in bucket:
            if slot:
                nums.extend(sorted(slot))

        ret = 0
        for i in range(0, N-1):
            ret = max(ret, nums[i+1] - nums[i])
        return ret Use bucket sort
