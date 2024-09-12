# LINT 803

from typing import (
    List,
)

from copy import deepcopy
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

class Solution:
    """
    @param grid: the 2D grid
    @return: the shortest distance
    """
    def shortest_distance(self, grid: List[List[int]]) -> int:
        # write your code here
        if not grid or not grid[0]:
            return 0

        building, freeland, obstacle = self.initial_count(grid)
        res = float('inf')
        for x, y in freeland:
            res = min(
                res,
                self.bfs(grid, building, obstacle, x, y),
            )
        if res == float('inf'):
            return -1
        return res

    def bfs(self, grid, building, obstacle, x, y):
        queue = collections.deque([(x, y)])
        visited = {(x, y): 0}
        distance = 0
        this_building = deepcopy(building)
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx, newy = x + dx, y + dy
                if not 0 <= newx < len(grid) or not 0 <= newy < len(grid[0]):
                    continue
                if (newx, newy) in visited:
                    continue
                if (newx, newy) in obstacle:
                    continue
                if (newx, newy) in this_building:
                    distance += visited[(x, y)] + 1
                    this_building.remove((newx, newy))
                    continue
                if (newx, newy) in building:
                    continue
                visited[(newx, newy)] = visited[(x, y)] + 1
                queue.append((newx, newy))
        if not this_building:
            return distance
        return float('inf')

    def initial_count(self, grid):
        building = set()
        freeland = set()
        obstacle = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    building.add((i, j))
                elif grid[i][j] == 0:
                    freeland.add((i, j))
                elif grid[i][j] == 2:
                    obstacle.add((i, j))

        return building, freeland, obstacle