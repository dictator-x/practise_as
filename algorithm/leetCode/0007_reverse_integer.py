# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        ret = 0

        a = abs(x)

        while a != 0:
            r = a % 10
            a = a // 10
            ret = ret * 10 + r

        if x > 0 and num < 2147483647:
            return ret
        elif x < 0 and num <= 2147483647:
            return -ret
        else:
            return 0
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(0))
