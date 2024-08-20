# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val2index = {}
        # Since all values are unique
        for i in range(len(inorder)):
            val2index[inorder[i]] = i

        return self.build(
            val2index, preorder, 0, len(preorder) - 1,
            inorder, 0, len(inorder) - 1,
        )

    def build(self, val2index, preorder, pstart, pend, inorder, istart, iend):
        if pstart > pend:
            return None

        rootval = preorder[pstart]
        index = val2index[rootval]
        
        leftsize = index - istart

        root = TreeNode(rootval)
        root.left = self.build(
            val2index, 
            preorder, pstart + 1, pstart + leftsize,
            inorder, istart, index - 1,
        )
        root.right = self.build(
            val2index, 
            preorder, pstart + leftsize + 1, pend,
            inorder, index + 1, iend,
        )
        return root