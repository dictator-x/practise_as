"""
407. Trapping Rain Water II
"""

from typing import List, Tuple
from heapq import heappush, heappop

class Checker:
    def __init__(self, heightMap: List[List[int]]):
        self.top_bound, self.left_bound = 0, 0;
        self.botton_bound = len(heightMap) - 1;
        self.right_bound = len(heightMap[0]) - 1;
        self.source = heightMap
        self.mask = [ [ 0 for _ in range(len(heightMap[j])) ] for j in range(len(heightMap)) ]

    def getValue(self, point: Tuple[int, int]) -> int:
        i, j = point
        return self.source[i][j]

    def isEdge(self, point: Tuple[int, int]) -> bool:
        i, j = point
        if i == self.top_bound or j == self.left_bound:
            return True
        elif i == self.botton_bound or j == self.right_bound:
            return True
        else:
            return False

    def isIndexOutOfArray(self, point: Tuple[int, int]) -> bool:
        i, j = point
        if i < self.top_bound or j < self.left_bound:
            return True
        elif i > self.botton_bound or j > self.right_bound:
            return True
        else:
            return False


    def mark(self, point: Tuple[int, int]):
        i, j = point
        self.mask[i][j] = 1

    def isMark(self, point: Tuple[int, int]):
        i, j = point
        return True if self.mask[i][j] == 1 else False

    def findUnpushedNeigbors(self, point: Tuple[int, int]) -> List[Tuple[int, int]]:
        ret = []
        i, j = point
        top, down, left, right = (i-1, j), (i+1, j), (i, j-1), (i, j+1)
        if not self.isIndexOutOfArray(top) and not self.isMark(top):
            ret.append(top)
        if not self.isIndexOutOfArray(down) and not self.isMark(down):
            ret.append(down)
        if not self.isIndexOutOfArray(left) and not self.isMark(left):
            ret.append(left)
        if not self.isIndexOutOfArray(right) and not self.isMark(right):
            ret.append(right)
        return ret


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        if not heightMap:
            return 0

        ret = 0
        c_max = 0
        checker = Checker(heightMap)
        heap = []
        row, column = len(heightMap), len(heightMap[0])

        for i in range(row):
            for j in range(column):
                point = (i, j)
                if checker.isEdge(point):
                    heappush(heap, (checker.getValue(point), point))
                    checker.mark(point)

        while len(heap) > 0:
            value, point = heappop(heap)
            if value > c_max:
                c_max = value

            neigbours = checker.findUnpushedNeigbors(point)
            for p in neigbours:
                if checker.getValue(p) < c_max:
                    ret += value - checker.getValue(p)
                    heappush(heap, (value, p))
                else:
                    heappush(heap, (checker.getValue(p), p))
                checker.mark(p)

        return ret




if __name__ == "__main__":
    m = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    solution = Solution()
    print(solution.trapRainWater(m))


