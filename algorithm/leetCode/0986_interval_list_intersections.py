"""
986. Interval List Intersections
"""

from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        ret = []

        while A and B:
            if A[0][1] < B[0][0]:
                A.pop(0)
            elif B[0][1] < A[0][0]:
                B.pop(0)
            else:
                l = max(A[0][0], B[0][0])
                r = min(A[0][1], B[0][1])
                ret.append([l, r])
                if B[0][1] > A[0][1]: A.pop(0)
                else: B.pop(0)
        return ret
