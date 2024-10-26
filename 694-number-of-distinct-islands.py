#  lint 860

from typing import (
    List,
)

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberof_distinct_islands(self, grid: List[List[int]]) -> int:
        # verify
        if not grid or not grid[0]:
            return 0
        
        visited = set()
        islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    island = self.bfs((i, j), visited, grid)
                    islands.add(island)
        return len(islands)

    def bfs(self, start, visited, grid):
        islandx = ['0']
        islandy = ['0']
        queue = collections.deque([start])
        visited.add(start)
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx = x + dx
                newy = y + dy
                if not 0 <= newx < len(grid) or not 0 <= newy < len(grid[0]):
                    continue
                if grid[newx][newy] != 1:
                    continue
                if (newx, newy) in visited:
                    continue
                islandx.append(str(newx - start[0]))
                islandy.append(str(newy - start[1]))
                queue.append((newx, newy))
                visited.add((newx, newy))
        return ','.join(islandx) + ';' + ','.join(islandy)