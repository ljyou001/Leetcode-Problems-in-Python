# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root.left and not root.right:
            return (root, 1)
        
        left_root, left_height = (root, 0)
        right_root, right_height = (root, 0)

        if root.left:
            left_root, left_height = self.dfs(root.left)
        if root.right:
            right_root, right_height = self.dfs(root.right)

        if left_height > right_height:
            return (left_root, left_height + 1)
        elif left_height < right_height:
            return (right_root, right_height + 1)
        else:
            return (root, left_height + 1)