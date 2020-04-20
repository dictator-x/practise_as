"""
315. Count of Smaller Numbers After Self
"""

from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #convert number into List[tuple[num, index]]
        items = []
        for index, value in enumerate(nums):
            items.append((value, index))

        ret = [ 0 for i in range(len(nums)) ]

        def merge(l1, h1, l2, h2):
            sorted_list=[]
            l = l1
            h = h2
            # in the left part if items[l1] > items[l2]
            # every nume between l1 and h1 will be greater than items[l2]
            # how to use accCounter is key of this algorithm
            accCounter = 0
            while l1 <= h1 and l2 <= h2:
                if items[l1][0] <= items[l2][0]:
                    ret[items[l1][1]] += accCounter
                    sorted_list.append(items[l1])
                    l1 += 1
                else:
                    accCounter += 1
                    sorted_list.append(items[l2])
                    l2 += 1

            while l1 <= h1:
                ret[items[l1][1]] += accCounter
                sorted_list.append(items[l1])
                l1 += 1

            while l2 <= h2:
                sorted_list.append(items[l2])
                l2 += 1

            # update items
            for item in sorted_list:
                items[l] = item
                l += 1

        def mergeSort(low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            mergeSort(low, mid)
            mergeSort(mid+1, high)
            merge(low, mid, mid+1, high)

        mergeSort(0, len(nums)-1)
        return ret

