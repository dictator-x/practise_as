"""
10. Regular Expression Matching
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_l = len(s)
        p_l = len(p)

        # create 2d metrix with extra 1 length, because will need to consider
        # empty string case.
        records = [ [ False for _ in range (s_l + 1) ] for _ in range (p_l + 1) ]

        # if pattern == "" and string == "", then the result should be true
        records[0][0] = True

        # compare empty string with any non-empty pattern, the result will always be false
        # compare pattern with empty string
        for i in range(1, p_l + 1):
            # "*" will not be at the beginning of the pattern.
            if ( p[i-1] == "*" ):
                # why it is based on i-2 position?
                # i-1 position contain char in front of *, like a* or .*
                # The current value really depends on anything pattern before .* or a*
                # eg: aa* will be false, because pattern a not match with empty string
                # eg: a*a* will be true, because pattern a* match with empty string
                records[i][0] = records[i-2][0]

        for i in range(1, p_l + 1):
            for j in range(1, s_l + 1):
                if s[j-1] == p[i-1] or p[i-1] == ".":
                    records[i][j] = records[i-1][j-1]
                elif p[i-1] == "*":
                    if s[j-1] == p[i-2] or p[i-2] == ".":
                        records[i][j] = (records[i-1][j] or records[i][j-1] or records[i-2][j])
                    else:
                        # pattern (...)a* vs string (...)
                        records[i][j] = records[i-2][j]

        return records[p_l][s_l]

if __name__ == "__main__":
    solution = Solution()
    print (solution.isMatch("aab", "c*a*b"))

