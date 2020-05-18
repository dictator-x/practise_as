"""
51. N-Queens
"""
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        rows = [False] * n
        cols = [False] * n
        # idx = i + j
        angle = [False] * (n*2 - 1)
        # idx = i - j + (n - 1)
        rangle = [False] * (n*2 - 1)
        grid = [ ["."] * n for _ in range(n) ]
        ret = []

        def available(i, j):
            if rows[i] or cols[j] or angle[i+j] or rangle[i-j+(n-1)]:
                return False
            return True

        def able(i, j):
            rows[i] = True
            cols[j] = True
            angle[i+j] = True
            rangle[i-j+(n-1)] = True

        def disable(i, j):
            rows[i] = False
            cols[j] = False
            angle[i+j] = False
            rangle[i-j+(n-1)] = False


        def search(r):
            if r >= n:
                ret.append([ "".join(i) for i in grid ])
                return

            for i in range(n):
                if available(r, i):
                    grid[r][i] = "Q"
                    able(r, i)
                    search(r+1)
                    grid[r][i] = "."
                    disable(r, i)
            return

        search(0)

        return ret
