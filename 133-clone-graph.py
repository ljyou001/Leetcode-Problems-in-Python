"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        queue = deque([node])
        val = node.val
        nodes = {
            node: Node(val=node.val)
        }
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in nodes:
                    nodes[neighbor] = Node(val=neighbor.val)
                    queue.append(neighbor)
                nodes[n].neighbors.append(nodes[neighbor])

        return nodes[node]

