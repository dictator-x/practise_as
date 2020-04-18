"""
1163. Last Substring in Lexicographical Order
"""

class Solution:
    def lastSubstring(self, s: str) -> str:
        if not s:
            return ""

        record = set([])
        m = "a"

        for c in s:
            if c > m:
                m = c

        for i in range(len(s)):
            if s[i] == m and ( i == 0 or s[i-1] != m):
                record.add(i)

        offset = 1

        while len(record) != 1:
            removed = []
            m = "a"
            for _, val in enumerate(record):
                if val+offset < len(s) and s[val+offset] > m:
                    m = s[val+offset]
            for index, val in enumerate(record):
                if val+offset >= len(s) or s[val+offset] != m:
                    removed.append(val)

            for val in removed:
                record.discard(val)
            offset += 1

        print(record)

        return s[next(enumerate(record))[1]:]

if __name__ == "__main__":
    s = "azeze"
    # s = "aaa"
    solution = Solution()
    print(solution.lastSubstring(s))
