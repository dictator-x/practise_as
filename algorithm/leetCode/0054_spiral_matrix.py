"""
54. Spiral Matrix
"""

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        seen = set()
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        N = len(matrix)
        M = len(matrix[0])

        ret = []
        d = 0
        i, j = 0, 0
        for _ in range(N*M):
            ret.append(matrix[i][j])
            seen.add((i, j))

            ni = i + direction[d][0]
            nj = j + direction[d][1]

            if ni < 0 or ni >= N or nj < 0 or nj >= M or (ni, nj) in seen:
                d = (d+1) % 4
                ni = i + direction[d][0]
                nj = j + direction[d][1]

            i, j = ni, nj
        return ret
