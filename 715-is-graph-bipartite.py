# LINT 1031

class VisitedType:
    NOT_VISITED = 0
    EVEN_SET = 1
    ODD_SET = -1

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        visited = [VisitedType.NOT_VISITED] * len(graph)
        for i in range(len(visited)):
            if visited[i] == VisitedType.NOT_VISITED:
                if not self.bfs(graph, visited, i):
                    return False
        return True

    def bfs(self, graph, visited, start):
        queue = deque([start])
        visited[start] = VisitedType.EVEN_SET
        while queue:
            node = queue.popleft()
            nodetype = visited[node]
            for neighbor in graph[node]:
                if visited[neighbor] == nodetype:
                    return False
                elif visited[neighbor] == nodetype * -1:
                    continue
                visited[neighbor] = nodetype * -1
                queue.append(neighbor)
        return True
