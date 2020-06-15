"""
493. Reverse Pairs
"""

from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        N = len(nums)

        # merge between [start, middle-1] and [middle, end]
        def merge(start, middle, end):
            p, q = start, middle+1
            ret = 0
            temp = [0] * (end - start + 1)
            # Calculate answer for this question.
            while p <= middle and q <= end:
                if nums[p] > 2*nums[q]:
                    ret += middle - p + 1
                    q += 1
                else:
                    p += 1

            # Do merge sort
            p, q = start, middle+1
            i = 0
            while p <= middle and q <= end:
                if nums[p] < nums[q]:
                    temp[i] = nums[p]
                    p += 1
                else:
                    temp[i] = nums[q]
                    q += 1
                i += 1

            while p <= middle:
                temp[i] = nums[p]
                p += 1
                i += 1

            while q <= end:
                temp[i] = nums[q]
                q += 1
                i += 1

            i = 0
            for j in range(start, end+1):
                nums[j] = temp[i]
                i += 1
            return ret

        def mergeSort(start, end):
            if start >= end: return 0

            m = start + (end-start) // 2
            ret = mergeSort(start, m)
            ret += mergeSort(m+1, end)
            ret += merge(start, m, end)
            return ret

        ret = mergeSort(0, N-1)
        return ret
