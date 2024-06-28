"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
# 注意这道题目坑很多，节点形态，values的key-value和返回值跟题目描述不一样

class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        queue = collections.deque([node])
        visited = set([node])
        while queue:
            node = queue.popleft()
            if values[node] == target:
                return node
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
        return None
