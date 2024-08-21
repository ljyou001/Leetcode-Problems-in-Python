# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SolutionPostorderTraversal:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum_val = 0
        self.traversal(root)
        return self.sum_val

    def traversal(self, root):
        if not root:
            return False
        if not root.left and not root.right:
            return True
        
        left = self.traversal(root.left)
        right = self.traversal(root.right)
        
        if left:
            self.sum_val += root.left.val


class SolutionInorderTraversal:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.traversal(root)

    def traversal(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        left = self.traversal(root.left)
        if root.left:
            if not root.left.left and not root.left.right:
                left += root.left.val

        right = self.traversal(root.right)
        
        return left + right
