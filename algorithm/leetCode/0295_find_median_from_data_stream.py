"""
295. Find Median from Data Stream
"""
from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):

        # max heap
        self.small_part = []
        # min heap
        self.large_part = []
        self.even = 1


    def addNum(self, num: int) -> None:
        if not self.small_part:
            heappush(self.small_part, -num)
        else:
            if self.even:
                if num <= self.large_part[0]:
                    heappush(self.small_part, -num)
                else:
                    heappush(self.small_part, -heappop(self.large_part))
                    heappush(self.large_part, num)
            else:
                if num >= -self.small_part[0]:
                    heappush(self.large_part, num)
                else:
                    heappush(self.large_part, -heappop(self.small_part))
                    heappush(self.small_part, -num)
        self.even ^= 1

    def findMedian(self) -> float:
        if self.even:
            return (-self.small_part[0] + self.large_part[0]) / 2
        else:
            return -self.small_part[0]
