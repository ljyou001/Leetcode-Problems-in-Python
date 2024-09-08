"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    def treeToDoublyList(self, root):
        if not root:
            return None

        dummy = TreeNode(0)
        cur = root
        tail = dummy
        stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()

            tail.right = cur
            cur.left = tail
            tail = cur
            
            cur = cur.right

        head = dummy.right
        head.left = tail
        tail.right = head
        return head