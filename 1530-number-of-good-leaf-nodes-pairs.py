# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self.dfs(root, distance)[1]

    def dfs(self, root, distance):
        if not root:
            return [], 0
        if not root.left and not root.right:
            return [1], 0
        
        left_leave, left_res = self.dfs(root.left, distance)
        right_leave, right_res = self.dfs(root.right, distance)
        res = left_res + right_res

        for left_dist in left_leave:
            for right_dist in right_leave:
                if left_dist + right_dist <= distance:
                    res += 1
        
        all_leave = left_leave + right_leave
        return [i + 1 for i in all_leave], res