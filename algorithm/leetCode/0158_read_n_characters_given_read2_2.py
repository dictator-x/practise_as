"""
158. Read N Characters Given Read4 II - Call multiple times
"""

class Solution:

    def __init__(self):
        self.cache = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        tmp = [''] * 4

        while len(self.cache) < n:
            i = read4(tmp)
            if not i: break
            self.cache.extend(tmp[:i])

        idx = 0
        while self.cache and idx < n:
            buf[idx] = self.cache.pop(0)
            idx += 1
        return idx
