"""
312. Burst Balloons
"""

from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]

        dp = [ [0] * (n+2) for _ in range(n+2) ]
        print (nums)
        print(dp)
        # sub list length
        for l in range(1, n+1):
            for i in range (1, n-l+1+1):
                j = i + l - 1
                for k in range (i, j+1):
                    print((l,i,j,k))
                    dp[i][j] = max(dp[i][j], nums[i-1]*nums[k]*nums[j+1] + dp[i][k-1] + dp[k+1][j])
                    print(dp)

        return dp[1][n]

if __name__ == "__main__":
    nums = [3,1,5,8]
    solution = Solution()
    print(solution.maxCoins(nums))
