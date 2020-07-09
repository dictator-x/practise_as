"""
621. Task Scheduler
"""

from typing import List
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        m_tasks = defaultdict(lambda: 0)

        for t in tasks:
            m_tasks[t] += 1

        tmp = sorted([ c for t, c in m_tasks.items() ])
        max_fre = tmp.pop()
        max_idle = (max_fre-1) * n

        while tmp and max_idle > 0:
            # handle two equal amount
            max_idle -= min(tmp.pop(), max_fre-1)
        max_idle = max(max_idle, 0)
        return len(tasks) + max_idle
