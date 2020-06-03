"""
1246. Palindrome Removal
"""

from typing import List

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        memo = {}

        def dfs(l, r):
            if l > r: return 0
            if (l, r) in memo: return memo[(l,r)]

            # Case 1: remove it self
            ret = 1 + dfs(l+1, r)

            # Case2: AxxxxxAxxxx
            # A...A can be deleted with the last operation of xxxxx.
            for i in range(l+1, r+1):
                if arr[i] == arr[l]:
                    # need to consider xxAAxx case.
                    ret = min(ret, dfs(l+1, i-1) + dfs(i+1, r) + (l+1 == i))
            memo[(l, r)] = ret
            return ret
        return dfs(0, len(arr)-1)

