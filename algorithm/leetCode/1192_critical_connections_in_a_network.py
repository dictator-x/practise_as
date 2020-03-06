"""
1192. Critical Connections in a Network
"""

from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        graph = collections.defaultdict(set)

        for e1, e2 in connections:
            graph[e1].add(e2)
            graph[e2].add(e1)

        visited = [-1] * n

        ret = []
        self.dfs(0, -1, 0, visited, ret, graph)
        return ret

    def dfs(self, cur, parent, level, visited, ret, graph):

        # give visited intial value
        visited[cur] = level + 1

        for n in graph[cur]:
            if n == parent:
                continue
            elif visited[n] == -1:
                # dfs
                visited[cur] = min(self.dfs(n, cur, level+1, visited, ret, graph), visited[cur])
            else:
                visited[cur] = min(visited[cur], visited[n])

        if visited[cur] == level + 1 and cur != 0:
            ret.append([parent, cur])

        return visited[cur]


