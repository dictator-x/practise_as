"""
465. Optimal Account Balancing
"""

from typing import List
import sys

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        accounts = {}

        for t in transactions:
            # Payer
            accounts[t[0]] = accounts.get(t[0], 0) + t[2]
            # Payee
            accounts[t[1]] = accounts.get(t[1], 0) - t[2]

        dp = []
        # We do not need to consider people whose balance is zero
        print(accounts)
        for key in accounts.keys():
            if accounts[key] != 0:
                dp.append(accounts[key])
        print(dp)

        def dfs(i, dp):
            if i >= len(dp):
                return 0

            # get value with index i
            cur = dp[i]
            # We do not need to consider 0 case, since it is already
            # balanced. We only need to consider remaining case.
            if cur == 0:
                return dfs(i+1, dp)

            min_value = sys.maxsize
            # swap i with remaining j, then calculate by dfs
            for j in range(i+1, len(dp)):
                # we should only consider one negative and one positive case.
                # guarantee dp[z] == 0 for z in [0, i]
                n = dp[j]
                if cur * n < 0:
                    dp[j] = cur + n
                    min_value = min(min_value, 1 + dfs(i+1, dp))
                    # restore j
                    dp[j] = n

            return min_value
        return dfs(0, dp)


