"""
41. First Missing Positive
"""

from typing import List
import sys

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_integer = sys.maxsize
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = max_integer
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if index >= 0 and index < len(nums) and nums[index] > 0:
                nums[index] = -nums[index]
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1

if __name__ == "__main__":
    nums = [1,2,0]
    solution = Solution()
    print(solution.firstMissingPositive(nums))

