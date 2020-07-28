"""
1188. Design Bounded Blocking Queue
"""

from threading import Semaphore, Lock

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.enqueueLock = Semaphore(capacity)
        self.dequeueLock = Semaphore(0)
        self.mutex = Lock()
        self.queue = []

    def enqueue(self, element: int) -> None:
        self.enqueueLock.acquire()
        self.mutex.acquire()
        self.queue.append(element)
        self.mutex.release()
        self.dequeueLock.release()

    def dequeue(self) -> int:
        self.dequeueLock.acquire()
        self.mutex.acquire()
        ret = self.queue.pop(0)
        self.mutex.release()
        self.enqueueLock.release()
        return ret

    def size(self) -> int:
        return len(self.queue)
