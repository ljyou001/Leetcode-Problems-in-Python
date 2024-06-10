# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []
        cur = root
        while inorder or cur:
            while cur:
                inorder.append(cur)
                cur = cur.left
            cur = inorder.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right