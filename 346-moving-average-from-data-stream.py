class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.numlist = collections.deque([])

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        self.numlist.append(val)
        if len(self.numlist) > self.size:
            self.numlist.popleft()
        return sum(self.numlist) / len(self.numlist)


class MovingAverage(object):
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.numlist = collections.deque([])
        self.total = 0

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        self.numlist.append(val)
        self.total += val
        if len(self.numlist) > self.size:
            dec_val = self.numlist.popleft()
            self.total -= dec_val
        return self.total/ len(self.numlist)
