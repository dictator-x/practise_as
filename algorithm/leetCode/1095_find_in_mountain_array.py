"""
1095. Find in Mountain Array
"""

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find peek index.
        n = mountain_arr.length()

        l, r = 0, n-1

        while l < r:
            m = l + (r-l) // 2
            value = mountain_arr.get(m)
            value_right = mountain_arr.get(m+1)
            print(value, value_right)
            if value_right > value:
                peek_index = m + 1
                l = m + 1
            else:
                # Do not use m-1
                # it will cause value miss
                r = m

        peek_value = mountain_arr.get(peek_index)
        if target > peek_value: return -1
        if target == peek_value: return peek_index

        l, r = 0, peek_index - 1
        while l <= r:
            m = l + (r-l) // 2
            value = mountain_arr.get(m)
            if value == target:
                return m
            elif value > target:
                r = m - 1
            else:
                l = m + 1

        l, r = peek_index + 1, n - 1
        while l <= r:
            m = l + (r-l) // 2
            value = mountain_arr.get(m)
            if value == target:
                return m
            elif value > target:
                l = m + 1
            else:
                r = m - 1
        return -1
