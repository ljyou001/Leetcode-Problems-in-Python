# LINT 614

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longest_consecutive2(self, root: TreeNode) -> int:
        return self.find_path(root)[0]

    def find_path(self, root):
        if not root:
            return 0, 0, 0
        leftmax, leftplus, leftminus = self.find_path(root.left)
        rightmax, rightplus, rightminus = self.find_path(root.right)
        rootplus, rootminus = 0, 0
        
        if root.left and root.left.val == root.val + 1:
            rootplus = leftplus + 1
        if root.right and root.right.val == root.val + 1:
            rootplus = max(rootplus, rightplus + 1)
        if root.left and root.left.val == root.val - 1:
            rootminus = leftminus + 1
        if root.right and root.right.val == root.val - 1:
            rootminus = max(rootminus, rightminus + 1)
        
        rootmax = max(
            leftmax,
            rightmax,
            rootplus + rootminus + 1
        )
        return rootmax, rootplus, rootminus