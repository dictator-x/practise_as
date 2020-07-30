"""
378. Kth Smallest Element in a Sorted Matrix
"""

from heapq import heappop, heappush
import sys

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = [(sys.maxsize, None, None)]
        i = 0
        ret = []

        while len(ret)<k:
            if i < len(matrix) and matrix[i][0] < min_heap[0][0]:
                for j in range(len(matrix[i])):
                    heappush(min_heap, (matrix[i][j],i,j))
                i += 1
            top = heappop(min_heap)
            ret.append(matrix[top[1]][top[2]])

        return ret[-1]
