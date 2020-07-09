"""
179. Largest Number
"""

#TODO: review again.
class LargestNumber(str):
    def __lt__(self, other):
        return self+other > other+self

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        ret = ''.join(sorted(map(str, nums), key=LargestNumber))
        return "0" if ret[0] == "0" else ret
