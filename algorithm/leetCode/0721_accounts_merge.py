"""
721. Accounts Merge
"""

from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_name = {}
        graph = defaultdict(set)

        for a in accounts:
            name = a[0]
            root = a[1]
            email_name[root] = name
            graph[root]

            for i in a[2:]:
                graph[root].add(i)
                graph[i].add(root)
                email_name[i] = name

        seen = set()
        ret = []
        for node in graph:
            if node not in seen:
                stack = [node]
                seen.add(node)
                ret_l = []
                while stack:
                    cur = stack.pop()
                    ret_l.append(cur)
                    for child in graph[cur]:
                        if child not in seen:
                            stack.append(child)
                            seen.add(child)
                ret.append([email_name[node]] + sorted(ret_l))
        return ret
