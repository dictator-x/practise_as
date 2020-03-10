"""
76. Minimum Window Substring
"""
import sys
from sets import Set

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        source = s
        match = t

        match_map = {}

        for c in match:
            if c not in match_map:
                match_map[c] = 1
            else:
                match_map[c] += 1


        sub = None
        length = sys.maxint
        count = 0
        start = 0

        for end in range(len(source)):
            c = source[end]
            if c not in match_map:
                continue

            match_map[c] -= 1
            # key point
            if match_map[c] >= 0:
                count += 1

            while count == len(match) and start <= end:
                if end - start + 1 < length:
                    length = end - start + 1
                    sub = (start, end)
                    print(sub)

                c = source[start]
                start += 1

                if c not in match_map:
                    continue

                match_map[c] += 1
                if match_map[c] == 1:
                    count -= 1

        return "" if sub == None else source[sub[0]:sub[1]+1]

