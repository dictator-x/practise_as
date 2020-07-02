"""
443. String Compression
"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = chars[0]
        count = 1
        write = 0

        for i in range(1, len(chars)):
            if cur != chars[i]:
                chars[write] = cur
                write += 1
                if count != 1:
                    # write count.
                    tmp = str(count)
                    for c in tmp:
                        chars[write] = c
                        write += 1
                count = 1
                cur = chars[i]
            else:
                count += 1

        chars[write] = cur
        write += 1
        if count != 1:
            # write count.
            tmp = str(count)
            for c in tmp:
                chars[write] = c
                write += 1

        return write
