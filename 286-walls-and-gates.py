# lint 663

class NodeTypes:
    WALL = -1
    GATE = 0
    ROOM = 2147483647

from copy import deepcopy
import collections

class Solution:
    def walls_and_gates(self, rooms: List[List[int]]):
        if not rooms or not rooms[0]:
            return []
        m, n = len(rooms), len(rooms[0])
        gates = self.find_gates(rooms)
        for x, y in gates:
            self.bfs(rooms, x, y)
        return rooms
        
    def find_gates(self, rooms):
        res = []
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == NodeTypes.GATE:
                    res.append((row, col))
        return res

    def is_valid(self, rooms, visited, x, y):
        if not (0 <= x < len(rooms) and 0 <= y < len(rooms[0])):
            return False
        if (x, y) in visited:
            return False
        return rooms[x][y] > 0

    def bfs(self, rooms, x, y):
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque([(x, y)])
        visited = set((x, y))
        while queue:
            curx, cury = queue.popleft()
            for dx, dy in DIRECTIONS:
                newx = curx + dx
                newy = cury + dy
                if self.is_valid(rooms, visited, newx, newy):
                    if rooms[newx][newy] > rooms[curx][cury] + 1:
                        rooms[newx][newy] = rooms[curx][cury] + 1
                        queue.append((newx, newy))
                        visited.add((newx, newy))