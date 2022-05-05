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