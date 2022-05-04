class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        result = []
        intervals.sort(key=lambda x: x[0])
        for i in intervals: # !!!
            if len(result) == 0 or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1]) 
        return result