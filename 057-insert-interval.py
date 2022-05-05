class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        result = []
        
        for i in intervals:
            if len(result) == 0 or result[-1][1] < i[0]:
                result.append(i)
            else:
                result[-1][1] = max(result[-1][1], i[1])
                
        return result