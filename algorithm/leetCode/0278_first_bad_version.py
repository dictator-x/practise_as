"""
278. First Bad Version
"""

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            md = lo + (hi-lo) // 2
            isGood = isBadVersion(md)
            if not isGood:
                lo = md+1
            else:
                hi = md

        return lo
