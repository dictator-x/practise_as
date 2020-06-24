"""
362. Design Hit Counter
"""

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [0] * 300
        self.times = [0] * 300


    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp % 300
        if self.times[idx] != timestamp:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        total = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total

