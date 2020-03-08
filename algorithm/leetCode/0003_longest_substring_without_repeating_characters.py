"""
3. Longest Substring Without Repeating Characters
"""

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        start = 0
        longest = 0

        for i in range(len(s)):
            if s[i] in record and record[s[i]] >= start:
                start = record[s[i]] + 1
            if i - start + 1 > longest:
                longest = i - start + 1
            record[s[i]] = i

        return longest

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("pwwkew"))
