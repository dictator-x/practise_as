"""
1152. Analyze User Website Visit Pattern
"""

from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = [(username[i], timestamp[i], website[i]) for i in range(len(username))]
        data.sort()

        user_website = defaultdict(list)
        for u, t, w in data:
            user_website[u].append(w)

        res = defaultdict(set)
        for u, ws in user_website.items():
            for p in combinations(ws, 3):
                res[p].add(u)

        return sorted(res.items(), key=lambda i:(-len(i[1]), i[0]))[0][0]

