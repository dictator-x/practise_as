"""
815. Bus Routes
"""
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        stop_to_bus = {}

        # create internal connection map.
        for i in range(len(routes)):
            for j in routes[i]:
                if j not in stop_to_bus:
                    stop_to_bus[j] = [i]
                else:
                    stop_to_bus[j].append(i)
        print(stop_to_bus)
        queue = [S]
        step = 0
        visited = set([])

        while queue:
            step += 1
            n = len(queue)
            for _ in range(n):
                stop = queue.pop(0)
                for bus in stop_to_bus[stop]:
                    if bus in visited: continue
                    for s in routes[bus]:
                        if s == T: return step
                        queue.append(s)
                    visited.add(bus)

        return -1
