"""
552. Student Attendance Record II
"""

class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * ( 4 if n <= 3 else n+1 )

        # Set initial value.
        # We count from index 1, so set index[0] to 1
        # And caculate without A first.
        dp[0] = 1
        dp[1] = 2 # two choice "P" or "L"
        dp[2] = 4 # four choice "PP", "LP", "LL", "PL"
        dp[3] = 7 # Total 8 combinations minus "LLL"

        for i in range(4, n+1):
            dp[i] = (dp[i-1] + dp[i-1] - dp[i-4]) % mod

        # caculate possible with A.
        ret = dp[n]
        for i in range(1, n+1):
            ret = (ret + dp[i-1] * dp[n-i]) % mod
        return ret
