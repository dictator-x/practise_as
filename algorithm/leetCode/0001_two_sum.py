"""
1. Two Sum
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use map record looped value.
        record = {}

        for i, n in enumerate(nums):
            remain = target - n
            if remain not in record:
                record[n] = i
            else:
                return [record[remain], i]

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
