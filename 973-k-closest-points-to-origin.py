from heapq import heappush, heappop, heapify


class SolutionHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        points = [(i[0]**2 + i[1]**2, [i[0], i[1]])
                    for i in points]
        heapify(points)
        for _ in range(k):
            res.append(heappop(points)[1])
        return res
    

class SolutionHeap2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for p in points:
            heappush(res, (-(p[0]**2 + p[1]**2), [p[0], p[1]]))
            if len(res) > k:
                heappop(res)
        return [i[1] for i in res]


class SolutionSort:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]