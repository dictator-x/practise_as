"""
336. Palindrome Pairs
"""

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def isPalindrome(s):
            s = [ char for char in s ]
            if len(s) <= 1:
                return True

            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        record = {}
        for i in range(len(words)):
            record[words[i]] = i

        ret = []
        for i in range(len(words)):
            for j in range(len(words[i])+1):
                l_part, r_part = words[i][0:j], words[i][j:]

                # Only left handle ["A", "A"] case
                if isPalindrome(l_part):
                    re = r_part[::-1]
                    if re in record and record[re] != i:
                        print(re)
                        ret.append([record[re], i])

                # key
                if r_part != "" and isPalindrome(r_part):
                    re = l_part[::-1]
                    if re in record and record[re] != i:
                        ret.append([i, record[re]])
        return ret

if __name__ == "__main__":
    words = ["abcd","dcba","lls","s","sssll"]
    # words = ["a",""]
    solution = Solution()
    print(solution.palindromePairs(words))
