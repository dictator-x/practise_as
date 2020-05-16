"""
1349. Maximum Students Taking Exam
"""

from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        # convert string to binary with . == 1 and # == 0
        seats = [int(''.join(s).replace('.','1').replace('#','0'),2) for s in seats]
        valids = []
        for i in range(2**n):
            bs = bin(i)[2:]
            # Any 11 is invalid
            if '11' not in bs:
                valids.append((i, bs.count('1')))

        # 2**n possibility in every row
        # column is possibility
        # TODO: why not use len(valid)
        dp = [ [ 0 for _ in range(2**n) ] for _ in range(m) ]
        # dp = [ [ 0 for _ in range(len(valids)) ] for _ in range(m) ]

        # Initial first row.
        for i, v in valids:
            if seats[0] & i == i:
                dp[0][i] = v

        for i in range(1, m):
            for j, v in valids:
                if seats[i] & j == j:
                    # Compare with previous row
                    for k, _ in valids:
                        if (j<<1) & k == 0 and (j>>1) & k == 0:
                            dp[i][j] = max(dp[i][j], v + dp[i-1][k])

        return max(dp[-1])

if __name__ == "__main__":
    seats = [["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]
    solution = Solution()
    print(solution.maxStudents(seats))
