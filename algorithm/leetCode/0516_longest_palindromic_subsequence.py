#516. Longest Palindromic Subsequence

from typing import List

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        max_length = 0
        dp_map = [ [ 0 for _ in range(length) ] for _ in range(length) ]

        # Initial value.
        for i in range(0, length):
            dp_map[i][i] = 1

        # Key here is loop from length of sub string.
        for sub_length in range(2, length+1):
            for i in range(0, length-sub_length+1):
                j = i+sub_length-1
                if s[i] == s[j] and sub_length == 2:
                    dp_map[i][j] = 2
                elif s[i] == s[j]:
                    dp_map[i][j] = dp_map[i+1][j-1] + 2
                else:
                    dp_map[i][j] = max(dp_map[i][j-1], dp_map[i+1][j])
        return dp_map[0][length-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindromeSubseq("bbbab"))
