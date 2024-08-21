# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        inorder2index = {}
        for i in range(len(inorder)):
            inorder2index[inorder[i]] = i
        return self.build(
            inorder2index,
            inorder, 0, len(inorder) - 1,
            postorder, 0, len(postorder) - 1,
        )

    def build(self, inorder2index, inorder, istart, iend, postorder, pstart, pend):
        if pstart > pend:
            return None
        
        node = TreeNode(postorder[pend])
        index = inorder2index[postorder[pend]]
        rightlen = iend - index
        node.right = self.build(
            inorder2index,
            inorder, index + 1, iend,
            postorder, pend - rightlen, pend - 1,
        )
        node.left = self.build(
            inorder2index,
            inorder, istart, index - 1,
            postorder, pstart, pend - rightlen - 1,
        )
        return node