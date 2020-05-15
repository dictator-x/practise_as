"""
352. Data Stream as Disjoint Intervals
"""
from typing import List

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []


    def addNum(self, val: int) -> None:
            newInterval = [val, val]
            ret = []
            for interval in self.intervals:
                if interval[1] < newInterval[0]-1:
                    ret.append(interval)
                elif interval[0] > newInterval[1]+1:
                    ret.append(newInterval)
                    newInterval = interval
                else:
                    newInterval[0] = min(newInterval[0], interval[0])
                    newInterval[1] = max(newInterval[1], interval[1])
            ret.append(newInterval)
            self.intervals = ret


    def getIntervals(self) -> List[List[int]]:
        return self.intervals
