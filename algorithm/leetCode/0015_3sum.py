"""
15. 3Sum
"""
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        if n < 3:
            return []

        ret = []

        for i in range(n - 2):
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            if nums[i] + nums[n-1] + nums[n-2] < 0:
                continue
            # If current number is equal to previous number, then ignore
            # Because this number is caculated already.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, h = i+1, n-1
            while l < h:
                if nums[i] + nums[l] + nums[h] == 0:
                    ret.append([nums[i], nums[l], nums[h]])
                    while l < h and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    while h > l and nums[h] == nums[h-1]:
                        h -= 1
                    h -= 1
                elif nums[i] + nums[l] + nums[h] < 0:
                    l += 1
                else:
                    h -= 1
        return ret

if __name__ == "__main__":
    solution = Solution()
    print (solution.threeSum([-1, 0, 1, 2, -1, -4]))
