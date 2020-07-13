"""
647. Palindromic Substrings
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0

        for i in range(0, 2*len(s)):
            left = i//2
            right = left + i%2

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                ret += 1

        return ret
