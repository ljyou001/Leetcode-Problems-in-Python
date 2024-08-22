# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxval, maxleft, maxright = self.dfs(root)
        return maxval

    def dfs(self, root):
        if not root:
            return float('-inf'), 0, 0
            # 之所以用 -inf 是因为有时候树的最大值不如0大
        
        left_val, left_left, left_right = self.dfs(root.left)
        right_val, right_left, right_right = self.dfs(root.right)

        maxleft = max(left_left, left_right, 0)
        maxright = max(right_left, right_right, 0)
        # 最后面的0是意味着如果任意一边加起来的值不如0大的话就不要了
        thisval = maxleft + maxright + root.val
        
        this_max = max(thisval, left_val, right_val)
        return this_max, maxleft + root.val, maxright + root.val