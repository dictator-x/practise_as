"""
1396. Design Underground System
"""

from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        print("ccc")

        self.checkInTime = {}
        self.journeyData = defaultdict(list)
        print("aac")

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTime[id] = (id, stationName, t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:

        enter = self.checkInTime[id]
        self.journeyData[(enter[1], stationName)].append(t-enter[2])
        del self.checkInTime[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.journeyData[(startStation, endStation)]) / len(self.journeyData[(startStation, endStation)])
