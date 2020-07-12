"""
311. Sparse Matrix Multiplication
"""

from typing import List

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        N = len(A)
        M = len(B[0])
        ret = [[0]*M for _ in range(N)]

        def cellCaculate(row, col):
            ret = 0
            for i in range(len(A[0])):
                ret += A[row][i]*B[i][col]
            return ret

        for i in range(N*M):
            d, m = divmod(i, len(A[0]))
            ret[d][m] = cellCaculate(d, m)

        return ret


