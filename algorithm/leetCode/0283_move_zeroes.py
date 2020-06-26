"""
283. Move Zeroes
"""

class Solution:
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0:
                j = i
                while j + 1 <= len(nums) - 1 and nums[j+1] != 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    j += 1
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for n in nums:
            if n != 0:
                nums[idx] = n
                idx += 1
        while idx < len(nums):
            nums[idx] = 0
            idx += 1
