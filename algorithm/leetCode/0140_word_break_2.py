"""
140. Word Break II
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wl = set(wordDict)
        mem = {}

        # Need to had copy prefixs
        def appends(prefixs, word):
            ret = []
            for prefix in prefixs:
                ret.append(prefix + " " + word)
            return ret

        def doWorkBreak(s):
            if s in mem:
                return mem[s][:]
            ret = []
            # Kind of ending point of recursive
            if s in wl:
                ret.append(s)

            # Entire String case has already been consider in above code.
            for i in range(len(s)-1, 0, -1):
                if s[i:] not in wl:
                    continue

                left_part_results = doWorkBreak(s[:i])
                ret += appends(left_part_results, s[i:])
            mem[s] = ret
            return mem[s]

        return doWorkBreak(s)

if __name__ == "__main__":
    test_arg1 = "catsanddog"
    test_arg2 = ["cat", "cats", "and", "sand", "dog"]
    test_arg1 = "pineapplepenapple"
    test_arg2 = ["apple","pen","applepen","pine","pineapple"]
    solution = Solution()
    print(solution.wordBreak(test_arg1, test_arg2))

