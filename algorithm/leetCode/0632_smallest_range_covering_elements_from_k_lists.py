"""
632. Smallest Range Covering Elements from K Lists
"""
from typing import List
import sys
from heapq import heappush, heappop

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_g, max_g = 0, sys.maxsize
        m = len(nums)
        rows_idx = [0] * m
        flag = True
        i = 0

        while i < m and flag:
            j = 0
            while j < len(nums[i]) and flag:
                print(i, j)
                # find min and max
                min_row, max_row = 0, 0
                for k in range(m):
                    if nums[k][rows_idx[k]] < nums[min_row][rows_idx[min_row]]:
                        min_row = k
                    if nums[k][rows_idx[k]] > nums[max_row][rows_idx[max_row]]:
                        max_row = k
                #print(nums[max_row][rows_idx[max_row]], nums[min_row][rows_idx[min_row]])
                # Calculate new range.
                if max_g - min_g > nums[max_row][rows_idx[max_row]] - nums[min_row][rows_idx[min_row]]:
                    max_g = nums[max_row][rows_idx[max_row]]
                    min_g = nums[min_row][rows_idx[min_row]]

                rows_idx[min_row] += 1

                if rows_idx[min_row] == len(nums[min_row]):
                    flag = False
                j += 1
            i += 1

        return [min_g, max_g]

        def smallestRange(self, nums: List[List[int]]) -> List[int]:
                min_g, max_g = 0, sys.maxsize
                m = len(nums)
                rows_idx = [0] * m
                flag = True

                heap = []

                max_l = -sys.maxsize
                for i in range(m):
                    heappush(heap, (nums[i][0],i))
                    max_l = max(max_l, nums[i][0])

                i = 0
                while i < m and flag:
                    j = 0
                    while j < len(nums[i]) and flag:
                        # find min and max
                        min_l, min_row = heappop(heap)

                        if max_g - min_g > max_l - min_l:
                            max_g = max_l
                            min_g = min_l

                        rows_idx[min_row] += 1

                        if rows_idx[min_row] == len(nums[min_row]):
                            flag = False
                            break

                        max_l = max(max_l, nums[min_row][rows_idx[min_row]])
                        heappush(heap, (nums[min_row][rows_idx[min_row]], min_row))
                        j += 1
                    i += 1

                return [min_g, max_g]

