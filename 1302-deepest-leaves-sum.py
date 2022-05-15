# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        q = deque([(root,1)])
        res = 0
        depth = 0
        while q:
            for i in range(len(q)):
                node, level = q.popleft()
                if level > depth: 
                    res = node.val
                    depth = level
                    print(1, level)
                else:
                    res += node.val
                    print(2, level)
                if node.left != None:
                    q.append((node.left, level + 1))
                if node.right != None:
                    q.append((node.right, level + 1))
                    
        return res