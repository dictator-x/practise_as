"""
895. Maximum Frequency Stack
"""

class FreqStack:

    def __init__(self):
        self.freqs = defaultdict(lambda: 0)
        self.stacks = [None]

    def push(self, x: int) -> None:
        freq = self.freqs[x] + 1
        if len(self.stacks) - 1 < freq : self.stacks.append([])
        self.stacks[freq].append(x)
        self.freqs[x] = freq

    def pop(self) -> int:
        if len(self.stacks) == 1: return -1

        ret = self.stacks[-1].pop()
        if not self.stacks[-1]: self.stacks.pop()
        self.freqs[ret] = self.freqs[ret] - 1
        if self.freqs[ret] == 0: del self.freqs[ret]
        return ret
