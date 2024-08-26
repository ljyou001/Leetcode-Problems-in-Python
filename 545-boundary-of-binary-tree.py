# LINT 878

class Solution:
    def boundary_of_binary_tree(self, root: TreeNode) -> List[int]:
        # write your code here
        if not root:
            return []

        # left
        left_node = []
        cur = root.left
        while cur:
            if cur.left or cur.right:
                left_node.append(cur.val)
            
            if cur.left:
                cur = cur.left
            elif cur.right:
                cur = cur.right
            else:
                break

        # right
        right_node = []
        cur = root.right
        while cur:
            if cur.left or cur.right:
                right_node.append(cur.val)

            if cur.right:
                cur = cur.right
            elif cur.left:
                cur = cur.left
            else:
                break

        # leaf
        leaf_node = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur != root and not cur.left and not cur.right:
                leaf_node.append(cur.val)
                
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)

        return [root.val] + left_node + leaf_node + right_node[::-1]
