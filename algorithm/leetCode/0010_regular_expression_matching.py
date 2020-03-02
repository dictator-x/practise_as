"""
10. Regular Expression Matching
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_l = len(s)
        p_l = len(p)

        records = [ [ False for _ in range (s_l + 1) ] for _ in range (p_l + 1) ]

        records[0][0] = True

        for i in range(1, p_l + 1):
            if ( p[i-1] == "*" ):
                records[i][0] = records[i-2][0]

        for i in range(1, p_l + 1):
            for j in range(1, s_l + 1):
                if s[j-1] == p[i-1] or p[i-1] == ".":
                    records[i][j] = records[i-1][j-1]
                elif p[i-1] == "*":
                    if s[j-1] == p[i-2] or p[i-2] == ".":
                        records[i][j] = (records[i-1][j] or records[i][j-1] or records[i-2][j])
                    else:
                        records[i][j] = records[i-2][j]

        return records[p_l][s_l]

if __name__ == "__main__":
    solution = Solution()
    print (solution.isMatch("aab", "c*a*b"))

