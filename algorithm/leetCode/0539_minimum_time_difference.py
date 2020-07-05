"""
539. Minimum Time Difference
"""

from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        temp = []

        for time in timePoints:
            s = time.split(":")
            temp.append(int(s[0])*60 + int(s[1]))

        temp.sort()
        return min( (y-x)%(24*60) for x, y in zip(temp, temp[1:]+temp[:1]) )
