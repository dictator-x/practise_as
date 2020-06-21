"""
49. Group Anagrams
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for s in strs:
            m["".join(sorted(s))].append(s)

        return [ i for i in m.values() ]
