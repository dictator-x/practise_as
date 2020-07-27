"""
131. Palindrome Partitioning
"""

from typing import List

#TODO: review.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return [ [s[:i]] + rest for i in range(1, len(s)+1) if s[:i] == s[i-1::-1] for rest in self.partition(s[i:]) ] or [[]]
