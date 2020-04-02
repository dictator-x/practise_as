"""
139. Word Break
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wl = set(wordDict)

        # Hint: why can use 1 D array?
        dp = [ 0 for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wl:
                    dp[i] = True

        return dp[len(s)]


if __name__ == "__main__":
    test_arg1 = "leetcode"
    test_arg2 = ["leet", "code"]
    solution = Solution()
    print(solution.wordBreak(test_arg1, test_arg2))

