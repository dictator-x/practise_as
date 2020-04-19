"""
301. Remove Invalid Parentheses
"""
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        patterns = [["(", ")"], [")", "("]]
        ret = []

        # remove extra ")"
        # then reverse remaining string
        # remove extra "("
        # if current string is invalid, it will return after remove a char and
        # test subString in dfs again.
        def dfs(pattern, s, start, lastRemovePosition):
            count = 0
            n = len(s)
            # We garantee that before start is valid in one pattern
            for i in range(start, n):
                if s[i] == pattern[0]:
                    count += 1
                if s[i] == pattern[1]:
                    count -= 1

                # If count is not >= 0, means current s is not a valid Parentheses
                # remove one extra char from string.
                # Then sub dfs method will check if remaining string is valid.
                if count < 0:
                    # Can j start from "start" instead of "lastRemovePosition"?
                    for j in range(lastRemovePosition, i+1):
                        char = s[j]
                        print(s)
                        # Only consider invalid char.
                        # sequence duplicate string are same, so do not need
                        # to consider. like "((((" or "))"
                        if char == pattern[1] and ( j == lastRemovePosition or char != s[j-1] ):
                            # i will be >=j
                            dfs(pattern, s[:j] + s[j+1:], i, j)

                    # We iterate the entire string until we find first unmatch position.
                    # It is safe to return at the position when we find first unmatch
                    return

            # The code can reach here
            # meaning that we have a valid string in one pattern
            # We do need to check another pattern.
            s = s[::-1]
            if pattern == patterns[0]:
                dfs(patterns[1], s, 0, 0)
            else:
                ret.append(s)

        dfs(patterns[0], s, 0, 0)
        return ret

if __name__ == "__main__":
    test_arg1 = "()))"
    solution = Solution()
    print(solution.removeInvalidParentheses(test_arg1))
