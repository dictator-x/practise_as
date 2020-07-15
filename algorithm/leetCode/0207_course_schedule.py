"""
207. Course Schedule
"""

from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        in_degree = defaultdict(lambda: 0)
        for s, e in prerequisites:
            graph[s].add(e)
            #Initial start
            in_degree[s]
            in_degree[e] += 1

        queue = [ k for k, v in in_degree.items() if v == 0]

        while queue:
            cur = queue.pop(0)

            for child in graph[cur]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)

        return True if sum([ v for _, v in in_degree.items()]) == 0 else False
