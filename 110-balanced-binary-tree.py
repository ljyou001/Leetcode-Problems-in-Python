# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return False if self.traversal(root) == -1 else True
        
    def traversal(self, root):
        if not root:
            return 0
        leftlevel = self.traversal(root.left)
        rightlevel = self.traversal(root.right)
        # Leaving Node Position
        if abs(leftlevel - rightlevel) > 1:
            return -1
        if leftlevel == -1 or rightlevel == -1:
            return -1
        return max(leftlevel, rightlevel) + 1