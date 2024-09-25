class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if not timePoints:
            return 0

        for i in range(len(timePoints)):
            time = timePoints[i].split(':')
            timePoints[i] = int(time[0]) * 60 + int(time[1])
        
        timePoints.sort()
        timePoints.append(timePoints[0] + 60 * 24)

        min_dif = float('inf')
        for i in range(len(timePoints) - 1):
            min_dif = min(min_dif, timePoints[i + 1] - timePoints[i])

        return min_dif