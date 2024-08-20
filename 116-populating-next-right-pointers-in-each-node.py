"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class SolutionBFS:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                node.next = None if i >= length - 1 else queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
        return root

class SolutionDivideNConqur:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        self.traverse(root.left, root.right)
        return root
    
    def traverse(self, node1, node2):
        if not node1 or not node2:
            return 
        
        node1.next = node2
        self.traverse(node1.left, node1.right)
        self.traverse(node1.right, node2.left)
        self.traverse(node2.left, node2.right)