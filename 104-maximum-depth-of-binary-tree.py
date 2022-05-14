# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 3 methods: Recursive, BFS, DFS


class Solution_Recursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)


class Solution_BFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root: return 0
        queue = deque([root])
        depth = 0
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                queue.append(node.left)
                queue.append(node.right)
        return depth

class Solution_DFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return res