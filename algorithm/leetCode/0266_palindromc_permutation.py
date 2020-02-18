# 266. Palindrome Permutation

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        record = [ 0 for _ in range(128) ]
        hasOdd = False

        for char in s:
            index = ord(char) - ord('a')
            record[index] = record[index] + 1

        for count in record:
            if count % 2 == 1:
                if hasOdd:
                    return False
                else:
                    hasOdd = True

        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.canPermutePalindrome("abb"))

