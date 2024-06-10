# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 1
        iterdfs = [(root, root.val)]
        while iterdfs:
            node, path_max = iterdfs.pop()
            if node.left:
                if node.left.val >= path_max:
                    res += 1
                    iterdfs.append((node.left, node.left.val))
                else:
                    iterdfs.append((node.left, path_max))
            if node.right:
                if node.right.val >= path_max:
                    res += 1
                    iterdfs.append((node.right, node.right.val))
                else:
                    iterdfs.append((node.right, path_max))
        return res