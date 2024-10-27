class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        
        reverse = trips[0][1] > trips[0][2]
        starts = []
        ends = []
        for persons, start, end in trips:
            if reverse:
                start *= -1
                end *= -1
            if start > end:
                return False

            starts.append((start, persons))
            ends.append((end, persons))
        
        starts.sort()
        ends.sort()
        i = 0
        j = 0
        incar = 0
        # (0 time, 1 person_num)
        while i < len(starts):
            while ends[j][0] <= starts[i][0]:
                incar -= ends[j][1]
                j += 1
            incar += starts[i][1]
            if incar > capacity:
                return False
            i += 1
        return True