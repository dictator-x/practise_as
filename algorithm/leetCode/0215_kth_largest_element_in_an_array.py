"""
215. Kth Largest Element in an Array
"""

from typing import List
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min heap.
        heap = []

        for idx, val in enumerate(nums):
            if idx >= k:
                if val > heap[0]:
                    heappop(heap)
                    heappush(heap, val)
            else:
                heappush(heap, val)

        return heap[0]
