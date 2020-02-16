# 88. Merge Sorted Array

class Solution:
    # count from the end
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        e1 = m - 1
        e2 = n - 1
        p = m + n - 1

        while e1 >= 0 and e2 >= 0:
            if nums1[e1] >= nums2[e2]:
                nums1[p] = nums1[e1]
                e1 -= 1
            else:
                nums1[p] = nums2[e2]
                e2 -= 1
            p -= 1

        while e2 >= 0:
            nums1[p] = nums2[e2]
            p -= 1
            e2 -= 1
