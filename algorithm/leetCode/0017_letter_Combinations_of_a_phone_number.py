"""
17. Letter Combinations of a Phone Number
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        phone = {
                    "2": ["a","b","c"],
                    "3": ["d","e","f"],
                    "4": ["g","h","i"],
                    "5": ["j","k","l"],
                    "6": ["m","n","o"],
                    "7": ["p","q","r","s"],
                    "8": ["t","u","v"],
                    "9": ["w","x","y","z"]
                }

        ret = []
        def doCombinate(prefix, remain):
            if len(remain) == 0:
                ret.append(prefix)
                return

            num = remain[0]

            for char in phone[num]:
                doCombinate(prefix+char, remain[1:])

        doCombinate("", digits)

        return ret

if __name__ == "__main__":
    solution = Solution()
    print(solution.letterCombinations("23"))

