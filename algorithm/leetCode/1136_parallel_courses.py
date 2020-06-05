"""
1136. Parallel Courses
"""

from typing import List
from collections import defaultdict

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        # Find in_degree.
        in_degree = { i: 0 for i in set(x for relation in relations for x in relation) }

        # Building graph
        graph = defaultdict(set)

        for relation in relations:
            graph[relation[0]].add(relation[1])
            in_degree[relation[1]] += 1

        #BFS
        queue = []
        for key, value in in_degree.items():
            if value == 0: queue.append(key)
        print(in_degree)
        ret = 0
        while queue:
            ret += 1
            n = len(queue)
            for _ in range(n):
                cur = queue.pop(0)
                for nei in graph[cur]:
                    if in_degree[nei] == 0: continue
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0: queue.append(nei)

        return ret if sum(in_degree.values()) == 0 else -1
