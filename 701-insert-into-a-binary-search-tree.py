# LINT 085

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionIter:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        cur = root
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
        return root

class SolutionRecur:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        if not root.left and val < root.val:
            root.left = TreeNode(val)
        if not root.right and val > root.val:
            root.right = TreeNode(val)
        if val < root.val:
            self.insertIntoBST(root.left, val)
        if val > root.val:
            self.insertIntoBST(root.right, val)
        return root