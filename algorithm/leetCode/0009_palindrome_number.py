"""
9. Palindrome Number
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        return True if x == int(str(x)[::-1]) else False
