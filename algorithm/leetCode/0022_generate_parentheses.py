"""
22. Generate Parentheses
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 0:
            return []

        ret = []

        def doGenerate(prefix, left, right):
            if left == n and right == n:
                ret.append(prefix)
                return

            if left == right:
                doGenerate(prefix+"(", left+1, right)
            else:
                if left != n:
                    doGenerate(prefix+"(", left+1, right)
                if right != n:
                    doGenerate(prefix+")", left, right+1)

        doGenerate("(", 1, 0)
        return ret

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(3))
