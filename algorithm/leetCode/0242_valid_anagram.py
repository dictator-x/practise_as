"""
242. Valid Anagram
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        record = [0] * 26

        for c in s:
            record[ord(c)-ord('a')] += 1

        for c in t:
            record[ord(c)-ord('a')] -= 1
            if record[ord(c)-ord('a')] < 0: return False

        return True
