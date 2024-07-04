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
    @return: the root of the minimum subtree
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        # write your code here
        self.res = root
        self.minsum = float('inf')

        self.recur(root)
        return self.res
    
    def recur(self, root):
        if not root:
            return 0
        leftsum = self.recur(root.left)
        rightsum = self.recur(root.right)
        thissum = leftsum + rightsum + root.val
        if thissum < self.minsum:
            self.minsum = thissum
            self.res = root
        return thissum
