"""
763. Partition Labels
"""

from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        record = defaultdict(lambda: -1)

        for idx, c in enumerate(S):
            record[c] = max(record[c], idx)

        end = 0
        start = 0
        ret = []
        for i, c in enumerate(S):
            end = max(end, record[c])
            if i == end:
                ret.append(end-start+1)
                start = end + 1
        return ret
