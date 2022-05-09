# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root,1)])
        depth = 0
        while q:
            node, depth_now = q.popleft()
            depth = max(depth,depth_now)
            if node.left == None and node.right == None:
                return depth
            if node.left != None:
                q.append((node.left, depth_now + 1))
            if node.right != None:
                q.append((node.right, depth_now + 1))

# This question showed how should you write a BFS algorithm