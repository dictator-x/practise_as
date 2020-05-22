"""
1074. Number of Submatrices That Sum to Target
"""

from typing import List

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        if not matrix: return 0

        n, m = len(matrix), len(matrix[0])

        pre = [ [0]*(m+1) for _ in range(n) ]
        for i in range(n):
            for j in range(1, m+1):
                pre[i][j] = pre[i][j-1] + matrix[i][j-1]

        def numSubarraySumTarget(presum, target):
            seen = {}
            ret = 0

            for psum in presum:
                if (psum - target) in seen:
                    ret += seen[psum - target]

                if psum in seen:
                    seen[psum] += 1
                else:
                    seen[psum] = 1
            return ret

        ret = 0
        for r1 in range(n):
            preSum = [0]*(m+1)
            for r2 in range(r1, n):
                for j in range(m+1):
                    preSum[j] = preSum[j] + pre[r2][j]
                ret += numSubarraySumTarget(preSum, target)

        return ret
