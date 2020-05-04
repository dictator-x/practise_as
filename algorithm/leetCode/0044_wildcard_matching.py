"""
44. Wildcard Matching
"""

# Use DP TOP Down
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dp(i, j, s, p, mem):
            if (i,j) in mem:
                return mem[(i,j)]

            if i == len(s) and j == len(p):
                return True

            # j == len(p) meaning there is no p to compare with s
            # so that return False
            if j == len(p):
                return False

            ret = False
            # consider case "aa" vs "aa****"
            if i == len(s):
                if p[j] == "*":
                    ret = dp(i, j+1, s, p, mem)
                else:
                    ret = False
            elif p[j] == "*":
                ret = dp(i+1, j, s, p, mem) or dp(i, j+1, s, p, mem) or dp(i+1, j+1, s, p, mem)
            elif s[i] == p[j] or p[j] == "?":
                ret = dp(i+1, j+1, s, p, mem)

            mem[(i,j)] = ret

            return ret

        return dp(0,0,s,p,{})
