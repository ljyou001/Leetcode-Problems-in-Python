# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        iterdfs = [(root, float('-inf'), float('inf'))]

        while iterdfs:
            node, level_min, level_max = iterdfs.pop()
            if node.val <= level_min or node.val >= level_max:
                return False
            if node.left:
                iterdfs.append((node.left, level_min, node.val))
            if node.right:
                iterdfs.append((node.right, node.val, level_max))
        return True