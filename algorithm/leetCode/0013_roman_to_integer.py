"""
13. Roman to Integer
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        r_s = s[::-1]
        total = value[r_s[0]]
        for i in range(1, len(r_s)):
            if value[r_s[i]] < value[r_s[i-1]]:
                total -= value[r_s[i]]
            else:
                total += value[r_s[i]]

        return total
