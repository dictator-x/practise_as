"""
125. Valid Palindrome
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ret = ""
        for c in s:
            if c.isalnum():
                ret += c
        return ret == ret[::-1]
