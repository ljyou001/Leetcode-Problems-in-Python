# LINT 900

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class SolutionBruteForce:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        if not root.left and not root.right:
            return root.val
        
        left_cloest = right_cloest = root.val
        if root.left:
            left_cloest = self.closest_value(root.left, target)
        if root.right:
            right_cloest = self.closest_value(root.right, target)
        
        abs_left = abs(target - left_cloest)
        abs_right = abs(target - right_cloest)
        abs_this = abs(target - root.val)

        if min(abs_left, abs_right, abs_this) == abs_left:
            return left_cloest
        if min(abs_left, abs_right, abs_this) == abs_right:
            return right_cloest
        return root.val
