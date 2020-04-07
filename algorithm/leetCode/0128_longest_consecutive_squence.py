"""
128. Longest Consecutive Sequence
"""
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        record = {}
        ret = 0
        for num in nums:
            if num in record:
                print(num)
                continue
            elif num-1 not in record and num+1 not in record:
                record[num] = 1
                ret = max(ret, record[num])
            elif num-1 in record and num+1 in record:
                l = record[num-1] + record[num+1] + 1
                record[num - 1 - record[num-1] + 1] = l
                record[num + 1 + record[num+1] - 1] = l
                record[num] = 1
                ret = max(ret, l)

            elif num-1 in record:
                record[num] = record[num-1] + 1
                record[num - 1 - record[num-1] + 1] = record[num-1] + 1
                ret = max(ret, record[num])
            elif num+1 in record:
                record[num] = record[num+1] + 1
                record[num + 1 + record[num+1] - 1] = record[num+1] + 1
                ret = max(ret, record[num])
        return ret
