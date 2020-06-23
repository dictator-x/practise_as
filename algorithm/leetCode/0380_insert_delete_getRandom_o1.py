"""
380. Insert Delete GetRandom O(1)
"""

from random import randrange

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.array = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        self.array.append(val)
        self.map[val] = len(self.array)-1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        idx = self.map[val]
        tail = self.array[-1]
        self.map[tail] = idx
        self.array[idx] = tail
        self.array.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.array: return -1
        rand = randrange(0, len(self.array))
        return self.array[rand]
