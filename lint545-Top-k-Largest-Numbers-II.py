import heapq

class Solution:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        elif self.heap[0] < num:
            heapq.heappush(self.heap, num)
            heapq.heappop(self.heap)
        
    def topk(self):
        return sorted(self.heap, reverse=True)