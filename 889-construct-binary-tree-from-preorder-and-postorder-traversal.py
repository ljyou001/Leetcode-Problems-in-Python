# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val2index = {}
        for i in range(len(postorder)):
            val2index[postorder[i]] = i
        return self.build(
            val2index,
            preorder, 0, len(preorder) - 1,
            postorder, 0, len(postorder) - 1,
        )

    def build(self, val2index, preorder, prestart, preend, postorder, poststart, postend):
        if prestart > preend:
            return None
        if prestart == preend:
            return TreeNode(preorder[prestart])

        rootval = preorder[prestart]
        leftval = preorder[prestart + 1]
        index = val2index[leftval]
        leftsize = index - poststart + 1

        root = TreeNode(rootval)
        root.left = self.build(
            val2index,
            preorder, prestart + 1, prestart + leftsize,
            postorder, poststart, index,
        )
        root.right = self.build(
            val2index,
            preorder, prestart + leftsize + 1, preend,
            postorder, index + 1, postend - 1,
        )
        return root