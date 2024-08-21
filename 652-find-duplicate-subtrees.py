# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memo = {}
        self.find(root, memo)
        res = []
        for times, node in memo.values():
            if times > 1:
                res.append(node)
        return res
        
    def find(self, root, memo):
        if not root:
            return '#'
        left = self.find(root.left, memo)
        right = self.find(root.right, memo)
        thistree = left + ',' + right + ',' + str(root.val)
        # 注意这一行是把str(root.val)放在最后，这主要是为了防止撞value
        if thistree in memo:
            memo[thistree][0] += 1
        else:
            memo[thistree] = [1, root]
        return thistree