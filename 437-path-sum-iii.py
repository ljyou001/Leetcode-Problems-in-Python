# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        self.count = 0
        prefix_sums = {0: 1} # sum: number
        
        self.traversal(root, 0, prefix_sums, targetSum)
        return self.count

    def traversal(self, root, prefix_sum, prefix_sums, targetSum):
        if not root:
            return
        
        prefix_sum += root.val
        if prefix_sum - targetSum in prefix_sums:
            self.count += prefix_sums[prefix_sum - targetSum]
        prefix_sums[prefix_sum] = prefix_sums.get(prefix_sum, 0) + 1
        
        # Why not here? In case of targetSum = 0
        # if prefix_sum - targetSum in prefix_sums:
        #     self.count += prefix_sums[prefix_sum - targetSum]
        
        self.traversal(root.left, prefix_sum, prefix_sums, targetSum)
        self.traversal(root.right, prefix_sum, prefix_sums, targetSum)
        
        prefix_sums[prefix_sum] -= 1
        prefix_sum -= root.val
        