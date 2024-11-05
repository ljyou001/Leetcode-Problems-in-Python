# LINT 3663

from typing import (
    List,
)

class Solution:
    """
    @param edges: Edges of an undirected tree.
    @return: Diameter of the undirected tree.
    """
    def undirected_tree_diameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0

        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        self.res = 0
        furtherest_node, _ = self.bfs(graph, 0)
        print(furtherest_node)
        _, diameter = self.bfs(graph, furtherest_node)
        return diameter

    def bfs(self, graph, start):
        queue = collections.deque([start])
        visited = {start: 0}
        furtherest_node = start
        longest_dist = 0
        while queue:
            node = queue.popleft()
            if longest_dist < visited[node]:
                furtherest_node = node
                longest_dist = visited[node]
            for child in graph[node]:
                if child in visited:
                    continue
                visited[child] = visited[node] + 1
                queue.append(child)
        return furtherest_node, longest_dist
