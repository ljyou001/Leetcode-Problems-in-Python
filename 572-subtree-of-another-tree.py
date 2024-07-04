# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        # if root.val == subRoot.val:
        #     return self.is_same_tree(root, subRoot)
        # Why above one is wrong:
        # Cuz if parent have a same value as children, 
        # it will not go to the children and check
        # This could be missing some Trues
        if self.is_same_tree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return True if left or right else False

    def is_same_tree(self, root, subroot):
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        if not root.val == subroot.val:
            return False
        
        return self.is_same_tree(root.left, subroot.left) \
            and self.is_same_tree(root.right, subroot.right)