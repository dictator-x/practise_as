"""
472. Concatenated Words
"""

from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:

        def doWorkBreak(s, wl):
            if not s:
                return False
            dp = [ False for _ in range(len(s)+1) ]
            dp[0] = True

            for i in range(1, len(s)+1):
                # j should not be equal to i
                # when j == 0, it takes care of whole string check
                for j in range(i):
                    # dp[j] record s[0:j-1]
                    if dp[j] == True and s[j:i] in wl:
                        dp[i] = True
                        break
            return dp[len(s)]

        wl = set(words)
        ret = []

        for word in words:
            wl.discard(word)
            if doWorkBreak(word, wl):
                ret.append(word)
            wl.add(word)
        return ret
