from typing import (
    List,
)

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Solution:
    """
    @param target_map: 
    @return: 
    """
    def shortest_path(self, target_map: List[List[int]]) -> int:
        # Write your code here
        if not target_map or not target_map[0]:
            return 0

        queue = collections.deque([(0, 0)])
        visited = {(0, 0): 0}
        while queue:
            x, y = queue.popleft()
            if target_map[x][y] == 2:
                return visited[(x, y)]
            for dx, dy in DIRECTIONS:
                newx, newy = x + dx, y + dy
                if not 0 <= newx < len(target_map):
                    continue
                if not 0 <= newy < len(target_map[0]):
                    continue
                if (newx, newy) in visited:
                    continue
                if target_map[newx][newy] == 1:
                    continue
                visited[(newx, newy)] = visited[(x, y)] + 1
                queue.append((newx, newy))
        return -1