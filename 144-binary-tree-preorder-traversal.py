# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionRecurDFS:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        if not root:
            return []
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        # Defining the end of the recursion
        if not root:
            return None

        # Before entering a node
        self.res.append(root.val)

        # Going to Enter a node
        self.dfs(root.left)
        self.dfs(root.right)

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res