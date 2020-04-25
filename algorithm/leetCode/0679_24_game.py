"""
679. 24 Game
"""
from typing import List

class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def operation(a, b):
            # remember to consider opposite case for minus and divide
            if a == 0 and b == 0:
                return [ a+b, a-b, a*b, b-a ]
            if a == 0:
                return [ a+b, a-b, a*b, a/b, b-a ]
            if b == 0:
                return [ a+b, a-b, a*b, b-a, b/a ]
            return [ a+b, a-b, a*b, a/b, b-a, b/a ]

        def doBackCheck(ds):
            if len(ds) == 1:
                return True if abs(ds[-1] - 24) < 0.00000001 else False

            # Build new sub list
            for i in range(len(ds)):
                for j in range(i+1, len(ds)):
                    nd = []
                    for k in range(len(ds)):
                        if k != i and k != j:
                            nd.append(ds[k])
                    ope = operation(ds[i], ds[j])
                    for z in range(len(ope)):
                        nd.append(ope[z])
                        if doBackCheck(nd):
                            return True
                        nd.pop()
            return False

        return doBackCheck(nums)
