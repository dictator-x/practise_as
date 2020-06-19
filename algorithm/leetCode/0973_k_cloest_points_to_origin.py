"""
973. K Closest Points to Origin
"""

from typing import List
from math import sqrt
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        temp = [ (sqrt(p[0]**2+p[1]**2), p) for p in points ]
        heap = []

        for idx, t in enumerate(temp):
            if idx >= K:
                if t[0] < abs(heap[0][0]):
                    heappop(heap)
                    heappush(heap, (-t[0], t[1]))
            else:
                heappush(heap, (-t[0], t[1]))

        return [ p[1] for p in heap ]
