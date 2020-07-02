"""
53. Maximum Subarray
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            ret = max(nums[i], ret)
        return ret
