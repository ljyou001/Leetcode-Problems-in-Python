"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            length = len(queue)
            this_layer = []
            for _ in range(length):
                node = queue.popleft()
                this_layer.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(this_layer)
        return res
