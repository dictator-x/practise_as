"""
287. Find the Duplicate Number
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # The question guarantee there is only one duplicate number.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
