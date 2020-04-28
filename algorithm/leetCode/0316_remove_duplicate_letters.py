"""
316. Remove Duplicate Letters
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dp = [ 0 for _ in range(26) ]
        visited = [ False for _ in range(26) ]

        for c in s:
            dp[ord(c) - ord('a')] += 1

        ret = []

        for c in s:
            if visited[ord(c) - ord('a')]:
                dp[ord(c) - ord('a')] -= 1
                continue

            while len(ret) > 0 and c < ret[-1] and dp[ord(ret[-1]) - ord('a')] > 0:
                    visited[ord(ret.pop()) - ord('a')] = False

            ret.append(c)
            dp[ord(c) - ord('a')] -= 1
            visited[ord(c) - ord('a')] = True
        return ''.join(ret)
