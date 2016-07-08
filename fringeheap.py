import heapq

class Fringeheap(object):
    """Fringeheap Class"""
    def __init__(self):
        super(Fringeheap, self).__init__()
        self.heap = []

    def enqueue(self, v):
        heapq.heappush(self.heap, v)

    def dequeue(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def isEmpty(self):
        return len(self.heap) <= 0
