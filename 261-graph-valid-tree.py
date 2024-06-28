# lint 178

class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        graph = [set() for _ in range(n)]
        visited = set()
        for src, dest in edges:
            graph[src].add(dest)
            graph[dest].add(src)
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor in visited:
                    return False
                graph[neighbor].remove(node)
                queue.append(neighbor)
                visited.add(neighbor)
        return len(visited) == n