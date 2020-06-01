"""
715. Range Module
"""

class RangeModule:

    def __init__(self):
        self.intervals = []


    def addRange(self, left: int, right: int) -> None:
        new_interval = (left, right)
        ret = []

        for interval in self.intervals:
            if interval[1] < new_interval[0]:
                ret.append(interval)
            elif interval[0] > new_interval[1]:
                ret.append(new_interval)
                new_interval = interval
            else:
                l = min(interval[0], new_interval[0])
                r = max(interval[1], new_interval[1])
                new_interval = (l, r)

        ret.append(new_interval)

        self.intervals = ret

    def queryRange(self, left: int, right: int) -> bool:
        n = len(self.intervals)
        l, r = 0, n-1

        while l <= r:
            m = l + (r-l) // 2
            if self.intervals[m][1] < left:
                l = m + 1
            elif self.intervals[m][0] > right:
                r = m - 1
            else:
                return self.intervals[m][0] <= left and self.intervals[m][1] >= right

        return False


    def removeRange(self, left: int, right: int) -> None:
        ret = []

        for interval in self.intervals:
            if interval[1] <= left or interval[0] >= right:
                ret.append(interval)
            else:
                if interval[0] < left:
                    ret.append((interval[0], left))
                if interval[1] > right:
                    ret.append((right, interval[1]))
        self.intervals = ret
