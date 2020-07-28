"""
18. 4Sum
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, target):
            ret = []
            lo, hi = 0, len(nums)-1
            while lo < hi:
                tmp = nums[lo] + nums[hi]
                if tmp == target:
                    ret.append([nums[lo], nums[hi]])
                    while lo < hi and nums[lo+1] == nums[lo]: lo += 1
                    while lo < hi and nums[hi-1] == nums[hi]: hi -= 1
                    hi -= 1
                    lo += 1
                elif tmp > target:
                    hi -= 1
                else:
                    lo += 1
            return ret

        nums.sort()
        n = len(nums)
        if n < 4: return []
        ret = []
        for i in range(n-3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i+1, n-2):
                    if j == i+1 or nums[j] != nums[j-1]:
                        two_sum_target = target - nums[i] - nums[j]
                        tmp = twoSum(nums[j+1:], two_sum_target)
                        if tmp:
                            ret.extend([[nums[i], nums[j]] + rest for rest in tmp if rest])

        return ret

