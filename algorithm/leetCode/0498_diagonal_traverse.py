"""
498. Diagonal Traverse
"""

from typing import List

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []

        even = True
        x, y = 0, 0
        ret = []
        for _ in range(len(matrix)*len(matrix[0])):
            ret.append(matrix[x][y])
            if even:
                nx, ny = x-1, y+1
                if ny >= len(matrix[0]):
                    x, y = x+1, y
                    even = False
                elif nx < 0:
                    x, y = x, y+1
                    even = False
                else:
                    x, y = nx, ny
            else:
                nx, ny = x+1, y-1
                if nx >= len(matrix):
                    x, y = x, y+1
                    even = True
                elif ny < 0:
                    x, y = x+1, y
                    even = True
                else:
                    x, y = nx, ny
        return ret
