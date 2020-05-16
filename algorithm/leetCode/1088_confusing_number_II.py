"""
1088. Confusing Number II
"""

class Solution:
    def confusingNumberII(self, N: int) -> int:
        count = 0

        values = [0, 1, 6, 8, 9]
        def reverse(val):
            ret = 0
            while val != 0:
                remain = val % 10
                val = val // 10
                if remain == 9: remain = 6
                elif remain == 6: remain = 9
                ret = ret*10 + remain
            return ret


        def search(val, mem):
            nonlocal count
            if val > N: return

            if val in mem: return

            val_reverse = reverse(val)
            if val_reverse != val:
                count = count + 1

            mem.add(val)

            for value in values:
                new_value = val*10 + value
                search(new_value, mem)

        search(0, set())
        return count

