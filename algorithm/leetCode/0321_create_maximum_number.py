"""
321. Create Maximum Number
"""
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def merge2List(nums1, nums2):
            ret = []
            while nums1 and nums2:
                if nums1 > nums2:
                    ret.append(nums1.pop(0))
                else:
                    ret.append(nums2.pop(0))

            ret.extend(nums1)
            ret.extend(nums2)
            return ret

        def findResult(nums, k):
            nums = nums[:]
            to_pop = len(nums) - k
            ret = []
            while nums:
                n = nums.pop(0)
                while ret and ret[-1] < n and to_pop > 0:
                    ret.pop()
                    to_pop -= 1
                ret.append(n)

            return ret[0:k]

        ret = []
        n1 = len(nums1)
        n2 = len(nums2)
        for k1 in range(k+1):
            k2 = k - k1
            if k1 > n1 or k2 > n2: continue
            ret = max(ret, merge2List(findResult(nums1, k1), findResult(nums2, k2)))

        return ret
