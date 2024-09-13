class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        res = []
        interval = [intervals[0][0], intervals[0][1]]
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start > interval[1]:
                res.append(interval[:])
                interval = [start, end]
            else:
                interval[1] = max(interval[1], end)
        
        res.append(interval[:])
        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[0])
        # attention here: lambda to do the sort
        for i in intervals: # !!!
            # Below here, we directly operate result[-1], in case for multiple intervals overlap
            if len(result) == 0 or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1]) 
        return result