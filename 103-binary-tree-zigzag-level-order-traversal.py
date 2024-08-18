# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        height = 1
        while queue:
            length = len(queue)
            this_layer = []
            for _ in range(length):
                node = queue.popleft()
                this_layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if height % 2 == 1:
                res.append(this_layer[:])
            else:
                res.append(this_layer[::-1])
            height += 1
        return res