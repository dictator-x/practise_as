"""
218. The Skyline Problem
"""

from typing import List
from heapq import heappop, heappush, heapify
import sys

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        class Event:
            def __init__(self, time, height, isEnter):
                self.time = time
                self.height = height
                self.isEnter = isEnter

            def __repr__(self):
                return "(time: {}, height: {}, type: {})".format(self.time,
                        self.height, "enter" if self.isEnter else "leave")

        b = []
        for building in buildings:
            b.append(Event(building[0],building[2], True))
            b.append(Event(building[1],building[2], False))

        # When time is same:
        # enter ... leave
        # when both leave:
        # lower ... higher
        # when both enter:
        # higher ... lower
        def buildingSort(event):
            if event.isEnter:
                return (event.time, 0, -event.height)
            else:
                return (event.time, 1, event.height)

        b.sort(key=buildingSort)
        min_value = -sys.maxsize
        heap = []
        ret = []
        for event in b:
            print(event)
            if event.isEnter:
                if not heap:
                    ret.append([event.time, event.height])
                    heappush(heap, -event.height)
                else:
                    peek = abs(heap[0])
                    if event.height > peek:
                        ret.append([event.time, event.height])
                    heappush(heap, -event.height)
            else:
                # Expensive: use other data struct to approve. like BST
                for i in range(len(heap)):
                    if abs(heap[i]) == event.height:
                        heap[i] = min_value
                        heapify(heap)
                        break
                heappop(heap)
                if not heap:
                    ret.append([event.time, 0])
                else:
                    if abs(heap[0]) < event.height:
                        ret.append([event.time, abs(heap[0])])
        return ret

if __name__ == "__main__":
    buildings = [[2,9,10],[2,9,15],[9,12,12],[15,20,10],[19,24,8]]
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    buildings = [[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]
    solution = Solution()
    print(solution.getSkyline(buildings))

