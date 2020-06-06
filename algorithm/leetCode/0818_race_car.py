"""
818. Race Car
"""
import sys

class Solution:
    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [sys.maxsize] * target

        for t in range(3, target+1):
            # 1, 2, 4, 8, 1....
            # eg. 8 < t < 16, then k == log2(8)
            k = t.bit_length()

            # if t in [1, 2, 4, 8, ... 2^k] - 1,
            # shortest step will be k
            if t == 2**k - 1:
                dp[t] = k
                continue

            # under t
            for i in range(k-1):
                dp[t] = min(dp[t], dp[t - 2**(k-1) + 2**i] + k - 1 + i + 2)

            # over t
            dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)

        return dp[target]
