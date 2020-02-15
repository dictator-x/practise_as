#4. Median of Two Sorted Arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            l_short, l_long = nums1, nums2
        else:
            l_short, l_long = nums2, nums1

        # Record length of each list
        l_short_len = len(l_short)
        l_long_len = len(l_long)

        # Calculate the number of integers that should be in the left-part
        # If total number of integers is odd, then left_part_nums = right_part_nums + 1
        left_part_nums = (l_short_len + l_long_len + 1) // 2

        l_short_binary_low = 0
        l_short_binary_high = l_short_len

        while l_short_binary_low <= l_short_binary_high:
            l_short_binary_mid = (l_short_binary_low + l_short_binary_high) // 2
            # Redeclare index(more clear).
            l_short_seperate = l_short_binary_mid
            l_long_seperate = left_part_nums - l_short_seperate

            # When condition [ l_short_seperate < l_shor_len ] or
            # [ l_short_seperate > 0 ] is true => extreme case
            # only need to consider two case:
            # 1. List1[l_short_seperate - 1] > List2[l_long_seperate] -> move left
            # 2. List1[l_short_sepetate] < List2[l_long_seperate - 1] -> move right

            if l_short_seperate < l_short_len and  l_long[l_long_seperate - 1] > l_short[l_short_seperate]:
                l_short_binary_low = l_short_seperate + 1
            elif l_short_seperate > 0 and l_short[l_short_seperate - 1] > l_long[l_long_seperate]:
                l_short_binary_high = l_short_seperate - 1
            else:
                break

        # There four extreme cases:

        if l_short_seperate == 0:
            max_left = l_long[l_long_seperate - 1]
        elif l_long_seperate == 0:
            max_left = l_short[l_short_seperate - 1]
        else:
            max_left = max(l_long[l_long_seperate - 1], l_short[l_short_seperate - 1])


        if (l_short_len + l_long_len) % 2 == 1:
            return max_left

        if l_short_seperate == l_short_len:
            min_right = l_long[l_long_seperate]
        elif l_long_seperate == l_long_len:
            min_right = l_short[l_short_seperate]
        else:
            min_right = min(l_long[l_long_seperate], l_short[l_short_seperate])


        return (max_left + min_right) / 2


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMedianSortedArrays([1,2], [-1,3]))
