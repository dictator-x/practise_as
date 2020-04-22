"""
340. Longest Substring with At Most K Distinct Characters
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        start, end = 0, 0
        n = len(s)
        count = 0
        dp = {}
        ret = 0

        for end in range(n):
            if s[end] not in dp:
                dp[s[end]] = 1
                count += 1
            else:
                dp[s[end]] += 1

            if count <= k:
                ret = max(ret, end - start + 1)

            while count > k and start < end:
                dp[s[start]] -= 1
                if dp[s[start]] <= 0:
                    del dp[s[start]]
                    count -= 1

                start += 1

        return ret

