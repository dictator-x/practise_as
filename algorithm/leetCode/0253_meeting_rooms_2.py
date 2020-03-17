"""
253. Meeting Rooms II
"""

from typing import List
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals or len(intervals) == 0:
            return 0

        sorted_internals = sorted(intervals, key = lambda interval: interval[0])

        heap = []

        heappush(heap, sorted_internals[0][1])

        for internal in sorted_internals[1:]:
            if internal[0] >= heap[0]:
                heappop(heap)

            heappush(heap, internal[1])

        return len(heap)


if __name__ == "__main__":
    solution = Solution()
    print (solution.minMeetingRooms([[0, 30],[5, 10],[15, 20]]))

