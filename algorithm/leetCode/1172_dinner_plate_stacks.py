"""
1172. Dinner Plate Stacks
"""
from heapq import heappush, heappop

class DinnerPlates:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.plates = []
        self.heap = []

    def push(self, val: int) -> None:
        while self.heap and self.heap[0] < len(self.plates) and len(self.plates[self.heap[0]]) == self.cap:
            heappop(self.heap)
        if not self.heap:
            heappush(self.heap, len(self.plates))
        # Why need seperate?
        # cause previoys while loop only remove till len(self.plates)
        # number that is bigger than len(self.plates) may still in the heap.
        if self.heap[0] == len(self.plates):
            self.plates.append([])
        self.plates[self.heap[0]].append(val)

    def pop(self) -> int:
        while self.plates and not self.plates[-1]:
            self.plates.pop()

        return self.popAtStack(len(self.plates)-1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.plates) and self.plates[index]:
            heappush(self.heap, index)
            return self.plates[index].pop()
        return -1

