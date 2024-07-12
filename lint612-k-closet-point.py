# LEET 973 https://leetcode.com/problems/k-closest-points-to-origin/description/

import heapq
class SolutionCorrect:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        heap = []
        for p in points:
            distance_sq = (origin.x - p.x) ** 2 + (origin.y - p.y) ** 2
            heapq.heappush(heap, (-distance_sq, -p.x, -p.y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append(Point(-x, -y))
        return res[::-1]

"""
Tricky part of this question:
NEED TO UNDERSTSAND: How heapq handle multiple values while pop sorting
It will compare the value one by one, if the 1st element is same, then 2nd, 3rd...
Example:
heap = [(1,2,3), (1,2,4), (1,3,3),(1,1,3)]
>>> heapq.heappop(heap)
(1, 1, 3)
>>> heapq.heappop(heap)
(1, 2, 3)
>>> heapq.heappop(heap)
(1, 2, 4)
>>> heapq.heappop(heap)
(1, 3, 3)
And always this order
"""

import heapq
class SolutionWRONG:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        heap = []
        for p in points:
            distance_sq = (origin.x - p.x) ** 2 + (origin.y - p.y) ** 2
            if len(heap) < k:
                heapq.heappush(heap, (-distance_sq, p))
            elif heap[0][0] < -distance_sq:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance_sq, p))
        res = []
        for _ in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res[::-1]

# WRONG:
# You must use heap to handle all elements in (-distance_sq, x, y)'s order

# Input Data
# [[-1,-1],[1,1],[100,100]]
# [0,0]
# 2
# Output Data
# [[1,1],[-1,-1]]
# Expected
# [[-1,-1],[1,1]]

import heapq
class SolutionWRONG:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def k_closest(self, points: List[Point], origin: Point, k: int) -> List[Point]:
        heap = []
        for p in points:
            distance_sq = (origin.x - p.x) ** 2 + (origin.y - p.y) ** 2
            if len(heap) < k:
                heapq.heappush(heap, (-distance_sq, -p.x, -p.y))
            elif heap[0][0] < -distance_sq:
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance_sq, -p.x, -p.y))
        res = []
        while heap:
            _, x, y = heapq.heappop(heap)
            res.append(Point(-x, -y))
        return res[::-1]

# WRONG:
# You did not use the heap to handle the order of (-distance_sq, x, y) while adding

# Input Data
# [[4,6],[4,6],[4,6],[-4,-6],[-4,6]]
# [0,0]
# 3
# Output Data
# [[4,6],[4,6],[4,6]]
# Expected
# [[-4,-6],[-4,6],[4,6]]