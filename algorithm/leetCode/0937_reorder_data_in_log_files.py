"""
937. Reorder Data in Log Files
"""

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted([log for log in logs if log[-1].isalpha()], key = lambda log: (log.split(" ", 1)[1], log.split(" ", 1)[0])) + [log for log in logs if not log[-1].isalpha()]
