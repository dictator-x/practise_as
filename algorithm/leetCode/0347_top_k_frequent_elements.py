"""
347. Top K Frequent Elements
"""

from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_fre = defaultdict(lambda: 0)
        for n in nums:
            val_fre[n] += 1

        buckets = [ [] for _ in range(len(nums)+1) ]

        for key, val in val_fre.items():
            buckets[val].append(key)

        ret = []
        i = k
        while k > 0:
            bucket = buckets.pop()
            ret.extend(bucket)
            k -= len(bucket)

        return ret
