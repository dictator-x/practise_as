"""
981. Time Based Key-Value Store
"""

from collections import defaultdict
from bisect import bisect

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        idx = bisect(self.map[key], (timestamp, chr(127)))
        return self.map[key][idx-1][1] if idx else ""


