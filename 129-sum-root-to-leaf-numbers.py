# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class SolutionRecursiveDFS:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.dfs(root, [root])

    def dfs(self, root, path):
        if not root.left and not root.right:
            number = ''
            for i in range(len(path)):
                number += str(path[i].val)
            return int(number)

        left_val = 0
        if root.left:
            path.append(root.left)
            left_val = self.dfs(root.left, path)
            path.pop()
        
        right_val = 0
        if root.right:
            path.append(root.right)
            right_val = self.dfs(root.right, path)
            path.pop()
            
        return left_val + right_val

