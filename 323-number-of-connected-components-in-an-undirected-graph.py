# LINT 3651

class SolutionBFS:
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        graph = self.build_graph(n, edges)
        count = 0
        while graph:
            self.bfs_count(graph)
            count += 1
        return count

    def build_graph(self, n, edges):
        graph = {
            i: set()
            for i in range(n)
        }
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)
        return graph

    def bfs_count(self, graph):
        start = list(graph.keys())[0]
        queue = collections.deque([start])
        visited = set([start])
        while queue:
            node = queue.pop()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
            del graph[node]
