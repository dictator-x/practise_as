"""
53. Maximum Subarray
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        max_v = num[0]

        while i < len(nums):
            if nums[i] > max_v:
                max_v = nums[i]
            if nums[i] > 0:
                break;
            i++


        acc = 0
        while i < len(nums):
            acc += nums[i]
            if acc < 0:
                acc = 0
            else:
                if acc > max_val:
                    max_v = acc

        return max_v

