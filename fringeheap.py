import heapq

class Fringeheap(object):
    """Fringeheap Class"""
    def __init__(self):
        super(Fringeheap, self).__init__()
        self.heap = []

    def push(self, v):
        heapq.heappush(self.heap, v)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def isEmpty(self):
        return len(self.heap) <= 0

    def contains(self, test):
        return test in self.heap
