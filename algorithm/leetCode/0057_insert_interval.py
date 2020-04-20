"""
57. Insert Interval
"""

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ls, rs = [], []
        newl, newr = newInterval[0], newInterval[1]

        for i in intervals:
            if i[1] < newl:
                ls.append(i)
            elif i[0] > newr:
                rs.append(i)
            else:
                newl = min(newl, i[0])
                newr = max(newr, i[1])

        return ls + [[newl, newr]] + rs
