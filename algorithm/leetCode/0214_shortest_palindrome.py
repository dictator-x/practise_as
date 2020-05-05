"""
214. Shortest Palindrome
"""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l, r = 0, len(s)-1
        end = len(s)-1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                l = 0
                end -= 1
                r = end

        return s[end+1:][::-1] + s

    def shortestPalindrome2(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s),-1,-1):
            if s[:i] == r[len(s)-i:]:
                break
        return t[:len(s)-i] + s
