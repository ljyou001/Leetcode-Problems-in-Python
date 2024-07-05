# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traversal(root, p, q)[0]
        
    def traversal(self, root, p, q):
        if not root:
            return None, False, False
        
        leftnode, leftp, leftq = self.traversal(root.left, p, q)
        rightnode, rightp, rightq = self.traversal(root.right, p, q)
        
        if leftp and leftq:
            return leftnode, leftp, leftq
        if rightp and rightq:
            return rightnode, rightp, rightq

        p_exist = leftp or rightp or root.val == p.val
        q_exist = leftq or rightq or root.val == q.val

        if p_exist and q_exist:
            return root, p_exist, q_exist
        return None, p_exist, q_exist