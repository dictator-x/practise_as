"""
381. Insert Delete GetRandom O(1) - Duplicates allowed
"""
from random import randint

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = {}
        self.list = []


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val not in self.hashTable:
            self.hashTable[val] = [len(self.list)]
            self.list.append([val, 0])
        else:
            self.hashTable[val].append(len(self.list))
            self.list.append([val, len(self.hashTable[val])-1])

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.hashTable:
            return False

        if self.hashTable[val][-1] != len(self.list) - 1:
            list_val_idx = self.hashTable[val][-1]

            self.list[list_val_idx][0] = self.list[-1][0]
            self.list[list_val_idx][1] = self.list[-1][1]

            self.hashTable[self.list[-1][0]][self.list[-1][1]] = list_val_idx

        self.list.pop()
        self.hashTable[val].pop()
        if not self.hashTable[val]: del self.hashTable[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        rand = randint(0, len(self.list)-1)
        return self.list[rand][0]
