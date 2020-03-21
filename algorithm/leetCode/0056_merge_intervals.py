"""
56. Merge Intervals
"""

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:    # sort list
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

        # do merge
        result_intervals = []
        for interval in sorted_intervals:
            if not result_intervals:
                result_intervals.append(interval)
            else:
                current_last_interval = result_intervals[-1]
                if current_last_interval[1] >= interval[0]:
                    if current_last_interval[1] < interval[1]:
                        current_last_interval[1] = interval[1]
                else:
                    result_intervals.append(interval)

        return result_intervals

if __name__ == "__main__":
    print (merge([[15,18], [1,3], [2,6], [8,10]]))
    print (merge([[1,4],[4,5]]))
