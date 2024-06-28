"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes: List[UndirectedGraphNode]) -> List[List[int]]:
        # write your code here
        visited = set()
        res = []
        for node in nodes:
            if node not in visited:
                res.append(self.bfs(node, visited))
        return res
    
    def bfs(self, node, visited):
        res = [node.label]
        queue = collections.deque([node])
        visited.add(node)
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                res.append(neighbor.label)
                queue.append(neighbor)
                visited.add(neighbor)
        return sorted(res)