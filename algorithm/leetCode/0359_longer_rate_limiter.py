"""
359. Logger Rate Limiter
"""

class Logger:

    def __init__(self):
        self.record = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.record:
            if timestamp - self.record[message] < 10:
                return false
            else:
                self.record[message] = timestamp
                return True
        else:
            self.record[message] = timestamp
            return True
