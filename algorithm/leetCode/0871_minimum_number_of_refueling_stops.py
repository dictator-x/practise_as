"""
871. Minimum Number of Refueling Stops
"""
from typing import List
from heapq import heappush, heappop

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stop = 0
        heap = []
        cur = startFuel
        i = 0

        while True:
            if cur >= target: return stop

            while i < len(stations) and cur >= stations[i][0]:
                heappush(heap, -stations[i][1])
                i += 1

            if not heap: break
            stop += 1
            cur += -heappop(heap)

        return -1
