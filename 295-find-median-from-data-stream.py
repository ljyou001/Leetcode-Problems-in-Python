from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        self.sn = []
        self.ln = []

    def addNum(self, num: int) -> None:
        if len(self.sn) == len(self.ln):
            heappush(self.sn, -num)
            if self.ln and self.sn[0] * -1 > self.ln[0]:
                heappush(self.sn, -heappop(self.ln))
                heappush(self.ln, -heappop(self.sn))
        elif len(self.sn) > len(self.ln):
            heappush(self.ln, num)
            if self.sn[0] * -1 > self.ln[0]:
                heappush(self.sn, -heappop(self.ln))
                heappush(self.ln, -heappop(self.sn))

    def findMedian(self) -> float:
        if len(self.sn) == len(self.ln):
            return (-self.sn[0] + self.ln[0]) / 2
        else:
            return -self.sn[0] 