"""
# Definition for a Node."""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        queue = deque([(root,1)])
        depth = 0
        while queue:
            depth += 1
            dummy = Node()
            for i in range(len(queue)):
                node, level = queue.popleft()
                dummy.next = node
                dummy = dummy.next
                if node.left: queue.append((node.left, depth+1))
                if node.right: queue.append((node.right, depth+1))
        return root