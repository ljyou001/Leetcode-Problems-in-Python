# Leet 295

# The difference of this question:
# It does not requires a actual median

import heapq

class Solution:
    def __init__(self):
        self.sn = []
        # Find the max
        self.ln = []
        # Find the min
    
    def add(self, val: int):
        if len(self.sn) <= len(self.ln):
            heapq.heappush(self.sn, -val)
        else:
            heapq.heappush(self.ln, val)
        if self.sn and self.ln and -self.sn[0] > self.ln[0]:
            ex_sn_val = -heapq.heappop(self.sn)
            ex_ln_val = heapq.heappop(self.ln)
            heapq.heappush(self.sn, -ex_ln_val)
            heapq.heappush(self.ln, ex_sn_val)

    def getMedian(self) -> int:
        # if len(self.sn) == len(self.ln):
        #     return -self.sn[0]
        # # ABOVE PART IS FOR ACTUAL MEDIAN NUM
        return -self.sn[0]