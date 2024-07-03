# LINT 597

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    node = None
    avg = 0

    def find_subtree2(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return self.node

    def dfs(self, root):
        if not root:
            return 0, 0
        
        left_sum, left_nodes = self.dfs(root.left)
        right_sum, right_nodes = self.dfs(root.right)

        this_sum = left_sum + right_sum + root.val
        this_nodes = left_nodes + right_nodes + 1

        if self.node is None or self.avg < this_sum / this_nodes:
            self.node = root
            self.avg = this_sum / this_nodes

        return this_sum, this_nodes