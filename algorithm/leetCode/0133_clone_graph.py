"""
133. Clone Graph
"""

class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None

        visited = { node: Node(node.val) }
        queue = [ node ]

        while len(queue) > 0:
            cur = queue.pop(0)

            for n in cur.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)

                visited[cur].neighbors.append(visited[n])

        return visited[node]
