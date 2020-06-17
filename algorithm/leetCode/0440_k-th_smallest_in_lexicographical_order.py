"""
440. K-th Smallest in Lexicographical Order
"""

# 1 <= k <= n <= 10^9
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Idea: go from possible parent to possible children

        def findGap(i, j, n):
            gap = 0
            while i <= n:
                gap += min(n+1, j) - i
                i *= 10
                j *= 10

            return gap

        cur = 1

        while k > 1:
            gap = findGap(cur, cur+1, n)
            if gap <= k-1:
                k -= gap
                cur += 1
            else:
                cur *= 10
                k -= 1

        return cur
