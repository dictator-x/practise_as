"""
706. Design HashMap
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.buckets = [ [] for _ in range(self.size) ]


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        bucket = self.buckets[idx]

        for b in bucket:
            if b[0] == key:
                b[1] = value
                return
        bucket.append([key, value])


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        bucket = self.buckets[idx]

        for b in bucket:
            if b[0] == key:
                return b[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        bucket = self.buckets[idx]
        idx = -1
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                idx = i
                break
        if idx != -1:
            bucket.pop(idx)
