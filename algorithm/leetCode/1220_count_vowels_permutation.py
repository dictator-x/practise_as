"""
1220. Count Vowels Permutation
"""

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        print(a,e,i,o,u)
        kmod = 10**9 + 7
        for k in range(2,n+1):
            aa = i + e + u
            ee = a + i
            ii = e + o
            oo = i
            uu = i + o

            a = aa
            e = ee
            i = ii
            o = oo
            u = uu

        return (a+e+i+o+u) % kmod
