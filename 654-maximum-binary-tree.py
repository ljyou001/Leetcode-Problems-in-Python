# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, start, end):
        if start > end:
            return None
        
        index = -1
        maxval = float('-inf')
        for i in range(start, end + 1):
            if maxval < nums[i]:
                index = i
                maxval = nums[i]

        root = TreeNode(
            maxval,
            self.build(nums, start, index - 1),
            self.build(nums, index + 1, end),
        )
        return root
