# LINT 919

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        # Write your code here
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        i = 0
        j = 0
        res = 0
        cur = 0
        while i < len(start):
            if start[i] < end[j]:
                cur += 1
                res = max(cur, res)
                i += 1
            elif end[j] < start[i]:
                cur -= 1
                res = max(cur, res)
                j += 1
            else:
                i += 1
                j += 1
        return res