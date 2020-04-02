#5. Longest Palindromic Substring

from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        start    = 0
        end      = 0

        # row and column represents any two point in the string
        dp_map = [ [ 0 for _ in range(s_length) ] for _ in range(s_length) ]

        # Initial dp_map
        for i in range(s_length):
            dp_map[i][i] = 1

        for sub_length in range(2, s_length + 1):
            for i in range(s_length - sub_length + 1):
                j = i + sub_length - 1
                if sub_length == 2:
                    if s[i] == s[j]:
                        dp_map[i][j] = 1
                        if start == 0 and end == 0:
                            start, end = i, j
                    else:
                        dp_map[i][j] = 0

                elif s[i] == s[j]:
                    dp_map[i][j] = dp_map[i+1][j-1]
                    if dp_map[i][j] == 1:
                        if j - i > end - start:
                            start, end = i, j

                else:
                    dp_map[i][j] = 0
        return s[start:end+1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("babad"))
