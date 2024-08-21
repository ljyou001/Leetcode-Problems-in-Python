# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root, [str(root.val)], res)
        return res
    
    def dfs(self, root, path, res):
        if not root.left and not root.right:
            return res.append('->'.join(path[:]))
        
        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, path, res)
            path.pop()

        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, path, res)
            path.pop()
