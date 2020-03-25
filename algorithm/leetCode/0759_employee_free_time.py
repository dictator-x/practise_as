"""
759. Employee Free Time
"""

class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for s in schedule:
            for interval in s:
                intervals.append(interval)

        if len(intervals) <= 0:
            return []

        sorted_schedule = sorted(intervals, key=lambda interval: interval.start)

        stack = [ sorted_schedule.pop(0) ]

        ret = []
        while len(sorted_schedule) > 0:
            top = stack[-1]
            cur = sorted_schedule.pop(0)

            if top.end < cur.start:
                ret.append(Interval(top.end, cur.start))
                stack.append(cur)
            else:
                top.start = min(top.start, cur.start)
                top.end = max(top.end, cur.end)

        return ret

