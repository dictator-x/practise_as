"""
239. Sliding Window Maximum
"""

from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if k > len(nums):
            return []

        mqueue = []

        def addToQueue(num):
            while len(mqueue) != 0 and mqueue[-1] < num:
                mqueue.pop()
            mqueue.append(num)

        i = 0

        while i < k:
            addToQueue(nums[i])
            i += 1
        print(mqueue)
        ret = [mqueue[0]]
        while i < len(nums):
            print(mqueue)
            j = i - k
            if nums[j] == mqueue[0]:
                mqueue.pop(0)

            addToQueue(nums[i])
            ret.append(mqueue[0])
            i += 1

        return ret

