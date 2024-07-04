# LINT 095

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionIterDFS:
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

class SolutionInOrder:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        inorder = []
        min_val = float('-inf')
        cur = root
        while inorder or cur:
            while cur:
                inorder.append(cur)
                cur = cur.left
            cur = inorder.pop()
            if cur.val <= min_val:
                return False
            min_val = cur.val
            cur = cur.right
        return True

class SolutionRecur:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dividenconqur(root, float('-inf'), float('inf'))

    def dividenconqur(self, root, minval, maxval):
        if not root:
            return True
        
        # Before entering the node 
        if not minval < root.val < maxval:
            return False
        # Entering the node
        left = self.dividenconqur(root.left, minval, root.val)
        right = self.dividenconqur(root.right, root.val, maxval)
        # After entering the node: pass values
        if not left or not right:
            return False
        return True