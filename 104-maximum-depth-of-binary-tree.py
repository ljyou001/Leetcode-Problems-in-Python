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
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionDFSTemplate:
    res = 0
    depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            # END Point
            return 0
        
        # Before entering a node
        self.depth += 1
        self.res = max(self.res, self.depth)
        
        # Going into a node
        self.dfs(root.right)
        self.dfs(root.left)

        # After entering a node
        self.depth -= 1

class SolutionDivideNConqurTemplate:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Going into a node
        leftmax = self.maxDepth(root.left)
        rightmax = self.maxDepth(root.right)
        
        # After entering a node
        return 1 + max(leftmax, rightmax)