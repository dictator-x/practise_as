"""
393. UTF-8 Validation
"""

from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remain_bytes = 0

        for d in data:
            if remain_bytes == 0:
                if d >> 3 == 0b11110: remain_bytes = 3
                elif d >> 4 == 0b1110: remain_bytes = 2
                elif d >> 5 == 0b110: remain_bytes = 1
                elif d >> 7 == 0b0: remain_bytes = 0
                else: return False
            else:
                if d >> 6 != 0b10: return False
                remain_bytes -= 1

        return remain_bytes == 0

