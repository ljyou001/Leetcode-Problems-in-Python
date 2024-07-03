# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res, depth = self.dfs(root)
        return res

    def dfs(self, root):
        if not root:
            return 0, 0
            
        left_diameter, leftdepth = self.dfs(root.left)
        right_diameter, rightdepth = self.dfs(root.right)

        maxdiameter = max(
            leftdepth + rightdepth,
            left_diameter,
            right_diameter,
        )
        return maxdiameter, max(leftdepth, rightdepth) + 1