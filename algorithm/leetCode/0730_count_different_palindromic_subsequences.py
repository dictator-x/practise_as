"""
730. Count Different Palindromic Subsequences
"""
class Solution:
    def countPalindromicSubsequences(self, S: str) -> int:
        memo = {}
        mod = 10 ** 9 + 7
        def search(s):
            if s == "": return 0
            if len(s) == 1: return 1
            if s in memo: return memo[s]

            if s[0] == s[-1]:
                l, r = 1, len(s)-2
                while l <= r and s[l] != s[0]: l += 1
                while l <= r and s[r] != s[0]: r -= 1

                if l > r: ret = 2 * search(s[1:-1]) + 2
                elif l == r: ret = 2 * search(s[1:-1]) + 1
                else: ret = 2 * search(s[1:-1]) - search(s[l+1:r])

            else:
                ret = search(s[:-1]) + search(s[1:]) - search(s[1:-1])

            memo[s] = ret
            return ret
        return search(S) % mod
